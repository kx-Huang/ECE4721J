# Homework 3: Ex.1

## Usage

Run MapReduce task with `Java` and `Apache Hadoop`

- Source File: `src/main/java/com/ve472/h3/MaxGrade.java`

- Remark: remove input and output folder on HDFS before running Mapreduce task

  ```bash
  hdfs dfs -rm -r -f /kexuan/h3e1/input
  hdfs dfs -rm -r -f /kexuan/h3e1/output
  ```

- Input: copy input CSV file to HDFS input folder

  ```bash
  hdfs dfs -put input/grades_100.csv /kexuan/h3e1/input
  ```

- Compile `Java` code:

  ```bash
  mvn package
  ```

- Run MapReduce task:

  ```bash
  hadoop jar target/ex1-1.0-SNAPSHOT.jar /kexuan/h3e1/input /kexuan/h3e1/output
  ```

- Output: get output file from HDFS

  ```bash
  hdfs dfs -get /kexuan/h3e1/output/
  ```

## Run single task with `make`

- Compile and run: `$ make`
- Input: CSV in local file `input/grades_100.csv`
- Output: Mapreduce result in local file `output/part-r-00000`

## Benchmark with `benchmark.sh`

Get runtime with 6 files with different line numbers: 1000 to 100000000

- Command:
  ```bash
  cd benchmark
  chomd +x benchmark.sh
  ./benchmark.sh
  ```
- Input: local folder `input/grades_<NUM>.csv`
- Output:
  1. Mapreduce result: local folder `output/<NUM>.out`
  2. Time log: local folder `log/time.log`

## Reference

1. [Apache Hadoop 3.3.3 MapReduce Tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html#Mapper)
