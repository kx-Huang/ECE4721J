package com.ve472.h3;

import avro.AvroFile;

import java.io.IOException;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.StandardCharsets;

import org.apache.avro.Schema;
import org.apache.avro.mapred.AvroKey;
import org.apache.avro.mapred.AvroValue;
import org.apache.avro.mapreduce.AvroJob;
import org.apache.avro.mapreduce.AvroKeyInputFormat;
import org.apache.avro.mapreduce.AvroKeyValueOutputFormat;

import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class MaxGrade extends Configured implements Tool {
  public static class MaxGradeMapper
      extends Mapper<AvroKey<AvroFile>, NullWritable, Text, IntWritable> {
    // output key-value pair: studentID-grade
    private Text studentID = new Text();
    private IntWritable grade = new IntWritable(0);

    // decode avro file raw data
    private String decodeByte(ByteBuffer byteBuffer) throws CharacterCodingException {
      Charset charset = StandardCharsets.UTF_8;
      CharsetDecoder charsetDecoder = charset.newDecoder();
      CharBuffer charBuffer = charsetDecoder.decode(byteBuffer.asReadOnlyBuffer());
      return charBuffer.toString();
    }

    @Override
    public void map(AvroKey<AvroFile> key, NullWritable value, Context context)
        throws IOException, InterruptedException {
      String raw = decodeByte(key.datum().getFilecontent());
      String[] records = raw.split("\n");
      // split each line by comma
      for (String row : records) {
        String[] cols = row.split(",");
        // skip ill-formed line
        if (cols.length != 3)
          return;
        // get studentID and grade
        studentID.set(cols[1]);
        grade.set(Integer.parseInt(cols[2]));
        // submit output key-value pair
        context.write(studentID, grade);
      }
    }
  }

  public static class MaxGradeReducer
      extends Reducer<Text, IntWritable, AvroKey<CharSequence>, AvroValue<Integer>> {
    private int maxGrade = 0;

    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException {
      // get the max grade
      int maxGrade = 0;
      while (values.iterator().hasNext())
        maxGrade = Math.max(maxGrade, values.iterator().next().get());
      // generate the output studentID-maxGrade pair.
      context.write(new AvroKey<CharSequence>(key.toString()), new AvroValue<Integer>(maxGrade));
    }
  }

  public int run(String[] args) throws Exception {
    // initialize the mapreduce job
    Job job = new Job(getConf());
    job.setJarByClass(MaxGrade.class);
    job.setJobName("get max grade");

    // set input/output path
    FileInputFormat.setInputPaths(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    // set the input/output format
    job.setInputFormatClass(AvroKeyInputFormat.class);
    job.setOutputFormatClass(AvroKeyValueOutputFormat.class);

    // set the output key/value class
    job.setMapOutputKeyClass(Text.class);
    job.setMapOutputValueClass(IntWritable.class);

    // set the mapper/reducer classes
    job.setMapperClass(MaxGradeMapper.class);
    job.setReducerClass(MaxGradeReducer.class);

    // set Avro input/output schema
    AvroJob.setInputKeySchema(job, AvroFile.getClassSchema());
    AvroJob.setOutputKeySchema(job, Schema.create(Schema.Type.STRING));
    AvroJob.setOutputValueSchema(job, Schema.create(Schema.Type.INT));

    // run the mapreduce job and wait for completion
    return (job.waitForCompletion(true) ? 0 : 1);
  }

  public static void main(String[] args) throws Exception {
    int res = ToolRunner.run(new MaxGrade(), args);
    System.exit(res);
  }
}
