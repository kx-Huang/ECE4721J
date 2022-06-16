package com.ve472.h3;

import avro.AvroFile;

import java.io.IOException;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.StandardCharsets;

import org.apache.avro.*;
import org.apache.avro.Schema.Type;
import org.apache.avro.mapred.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class MaxGrade extends Configured implements Tool {

    public static class MaxGradeMapper extends AvroMapper<AvroKey<AvroFile>, Pair<CharSequence, Integer>> {

        private Text studentID = new Text();
        private Integer grade = new Integer(0);

        // decode avro file raw data
        private String decodeByte(ByteBuffer byteBuffer) throws CharacterCodingException {
            Charset charset = StandardCharsets.UTF_8;
            CharsetDecoder charsetDecoder = charset.newDecoder();
            CharBuffer charBuffer = charsetDecoder.decode(byteBuffer.asReadOnlyBuffer());
            return charBuffer.toString();
        }

        @Override
        public void map(AvroKey<AvroFile> key, AvroCollector<Pair<CharSequence, Integer>> collector, Reporter reporter) throws IOException {
            String raw = decodeByte(key.datum().getFilecontent());
            String[] records = raw.split("\n");
            // split each line by comma
            for (String row : records) {
                String[] cols = row.split(",");
                // skip ill-formed line
                if (cols.length != 3) return;
                // get studentID and grade
                studentID.set(cols[1]);
                grade.set(Integer.parseInt(cols[2]));
                // submit output key-value pair
                collector.collect(new Pair<CharSequence, Integer>(studentID, grade));
            }
        }
    }

    public static class MaxGradeReducer extends AvroReducer<CharSequence, Integer,
                                                            Pair<CharSequence, Integer>> {
        @Override
        public void reduce(CharSequence key, Iterable<Integer> values,
                       AvroCollector<Pair<CharSequence, Integer>> collector,
                       Reporter reporter) throws IOException {
            // get the max grade
            Integer maxGrade = new Integer(0);
            while (values.iterator().hasNext())
                maxGrade = Math.max(maxGrade, values.iterator().next().get());
            // generate the output studentID-maxGrade pair.
            collector.collect(new Pair<CharSequence, Integer>(key, maxGrade));
        }
    }

    public int run(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: MaxGrade <input path> <output path>");
            return -1;
        }

        // initialize the mapreduce job
        JobConf conf = new JobConf(getConf(), MaxGrade.class);
        conf.setJobName("get max grade");

        // set input/output path
        FileInputFormat.setInputPaths(conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));

        // set the mapper/reducer classes
        AvroJob.setMapperClass(conf, MaxGradeMapper.class);
        AvroJob.setReducerClass(conf, MaxGradeReducer.class);

        // set Avro input/output schema
        AvroJob.setInputSchema(conf, AvroKey<AvroFile>.getClassSchema());
        AvroJob.setOutputSchema(conf, Pair.getPairSchema(Schema.create(Type.STRING),
        Schema.create(Type.INT)));

        // run the mapreduce job
        JobClient.runJob(conf);
        return 0;
    }

    public static void main(String[] args) throws Exception {
        int res = ToolRunner.run(new Configuration(), new MaxGrade(), args);
        System.exit(res);
    }
}
