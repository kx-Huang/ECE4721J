package com.ve472.h3;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MaxGrade {

    public static class Map
            extends Mapper<Object, Text, Text, IntWritable> {

        // initialize output key-value pair: studentID-grade
        private Text studentID = new Text();
        private IntWritable grade = new IntWritable(0);

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] entry = value.toString().split(",");
            // skip ill-formed line
            if (entry.length != 3)
                return;
            // get studentID and grade
            studentID.set(entry[1]);
            grade.set(Integer.parseInt(entry[2]));
            // submit output key-value pair
            context.write(studentID, grade);
        }
    }

    public static class Reduce
            extends Reducer<Text, IntWritable, Text, IntWritable> {

        // initialize output grade
        private IntWritable grade = new IntWritable(0);

        public void reduce(Text key, Iterable<IntWritable> values,
                Context context) throws IOException, InterruptedException {
            // get the max grade
            int maxGrade = 0;
            while (values.iterator().hasNext())
                maxGrade = Math.max(maxGrade, values.iterator().next().get());
            grade = new IntWritable(maxGrade);
            // generate the output studentID-maxGrade pair.
            context.write(key, grade);
        }

    }

    public static void main(String[] args) throws Exception {
        // initialize the job configuration
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "get max grade");

        // Set the Jar by finding where a given class came from.
        job.setJarByClass(MaxGrade.class);

        // set the mapper and reducer classes
        job.setMapperClass(Map.class);
        job.setCombinerClass(Reduce.class);
        job.setReducerClass(Reduce.class);

        // set the output key and value types
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // set input and output path
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // run and wait for job to finish
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
