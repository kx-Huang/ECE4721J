# Lab 2: Hadoop MapReduce

## 1. Generate Data

Script `generate.py` generates CSV file contains random names, studentsID and grades

- Run: `$ python3 generate.py <number of lines>`
  - e.g. `python3 generate.py 100`
- Python module: `names`, `random`
- Input: None
- Output: create directory `data/` and generate `grades_100.csv`
  - Format: `<name>,<studentID>,<grade>`
  - e.g. `Michael Huang,0123456789,90`

## 2. Mapper

Mapper reads `stdin` with name, studentID & grade separated by newline, and returns the tab-separated pair: `studentID<TAB>grade`

- Run: `$ ./mapper.sh`
- Input: `stdin` (e.g `Michael Huang,0123456789,100`)
- Output: `stdout` (e.g `0123456789<TAB>100`)
- Test: Use input redirection to read from file `grades.csv`

## 3. Reducer

Reducer reads tab-separated pairs from the standard input, each of which is composed of a studentID and a grade, and returns the max grade for each student on the standard output.

- Run: `$ ./reducer.py`
- Input: `stdin` (e.g. `0123456789<TAB>80 ... 0123456789<TAB>100`)
- Output: `stdout` (e.g. `0123456789 100`)

## 4. Single Task

Single task cascades mapper and reducer with pipes.

- Run: `$ cat data/grades_<NUM>.csv | ./mapper.sh | ./reducer.py`
- Benchmark: use `time` command to calculate time elapsed for CSV files with `<NUM>` lines

## 5. Hadoop Cluster

### a. HDFS (Hadoop Distributed File System)

```bash
hdfs dfs -ls <DFS_DIR>
hdfs dfs -mkdir <DFS_DIR>
hdfs dfs -put <LOCAL_DIR> <DFS_DIR>
hdfs dfs -get <DFS_DIR>
hdfs dfs -rm -r -f output
```

You can check via Utilities->Browse file system in `localhost:9870` to check the directory and files on the HDFS.

### b. Streaming

In your hadoop home directory, run streaming with package: `share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar` via the following command after you have created directory in HDFS for `<DFS_INPUT_DIR>` and `<DFS_OUTPUT_DIR>`

```bash
hadoop jar <HADOOP_HOME>/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -input <DFS_INPUT_DIR> -output <DFS_OUTPUT_DIR> -mapper <MAPPER> -reducer <REDUCER> -file <LOCAL_MAPPER_DIR>  -file <LOCAL_REDUCER_DIR>
```

*Note*:

- <MAPPER> and <REDUCER> can be local files, while <DFS_INPUT_DIR> and <DFS_OUTPUT_DIR> is in HDFS
- `<DFS_OUTPUT_DIR>` needs to be emptyed everytime re-running the MapReduce task

*Error Handling*:

- Check `<HADOOP_HOME>/logs` for detailed logs
- `WARN org.apache.hadoop.streaming.PipeMapRed: java.io.IOException`
  - Check if `#!/usr/bin/env python` is included if you are using `python`
  - Check if shell scripts are granted permission to execute
  - Check if shell scripts handle the exception correctly
