package com.ve472.h3;

import avro.AvroFile;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;

// hadoop
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;

// mapreduce
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

// avro
import org.apache.avro.Schema;
import org.apache.avro.mapred.AvroKey;
import org.apache.avro.mapred.AvroValue;
import org.apache.avro.mapreduce.AvroJob;
import org.apache.avro.mapreduce.AvroKeyInputFormat;
import org.apache.avro.mapreduce.AvroKeyValueOutputFormat;

// bloom filter
import org.apache.hadoop.util.bloom.BloomFilter;
import org.apache.hadoop.util.bloom.Key;
import org.apache.hadoop.util.hash.Hash;

public class FilterID extends Configured implements Tool {
  public static class FilterIDMapper
      extends Mapper<AvroKey<AvroFile>, NullWritable, NullWritable, BloomFilter> {
    // output key-value pair: studentID-grade
    private Text studentID = new Text();
    private IntWritable grade = new IntWritable(0);

    // set up bloom filter with around 1000 entries and 5 hash functions
    BloomFilter bf = new BloomFilter(1000, 5, Hash.MURMUR_HASH);

    @Override
    public void map(AvroKey<AvroFile> key, NullWritable value, Context context)
        throws IOException, InterruptedException {
      String raw = new String(key.datum().getFilecontent().array());
      String[] records = raw.split("\n");
      // split each line by comma
      for (String row : records) {
        String[] cols = row.split(",");
        // skip ill-formed line
        if (cols.length != 3)
          return;
        // get studentID and last bit
        String id = cols[1];
        String lastBit = id.substring(id.length() - 1);
        // add studentID only ends with a 3 to bloom filter
        if (lastBit.equals("3")) {
          studentID.set(id);
          Key filterKey = new Key(studentID.getBytes());
          bf.add(filterKey);
        }
        // submit the bloom filter
        context.write(NullWritable.get(), bf);
      }
    }
  }

  public static class FilterIDReducer
      extends Reducer<NullWritable, BloomFilter, AvroKey<CharSequence>, NullWritable> {
    // bloom filter
    BloomFilter bf = new BloomFilter(1000, 5, Hash.MURMUR_HASH);

    @Override
    public void reduce(NullWritable key, Iterable<BloomFilter> values, Context context)
        throws IOException, InterruptedException {
      // Merge all bloom filters by logical OR
      for (BloomFilter value : values) bf.or(value);
      // serialize bloom filter to avro file
      DataOutputStream buffer = new DataOutputStream(new ByteArrayOutputStream());
      bf.write(buffer);
      context.write(new AvroKey<CharSequence>(buffer.toString()), NullWritable.get());
    }
  }

  public int run(String[] args) throws Exception {
    // initialize the mapreduce job
    Job job = new Job(getConf());
    job.setJarByClass(FilterID.class);
    job.setJobName("filter ID ends with 3");

    // set input/output path
    FileInputFormat.setInputPaths(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    // set the input/output format
    job.setInputFormatClass(AvroKeyInputFormat.class);
    job.setOutputFormatClass(AvroKeyValueOutputFormat.class);

    // set the output key/value class
    job.setMapOutputKeyClass(NullWritable.class);
    job.setMapOutputValueClass(BloomFilter.class);

    // set the mapper/reducer classes
    job.setMapperClass(FilterIDMapper.class);
    job.setReducerClass(FilterIDReducer.class);

    // set Avro input schema
    AvroJob.setInputKeySchema(job, AvroFile.getClassSchema());

    // run the mapreduce job and wait for completion
    return (job.waitForCompletion(true) ? 0 : 1);
  }

  public static void main(String[] args) throws Exception {
    int res = ToolRunner.run(new FilterID(), args);
    System.exit(res);
  }
}
