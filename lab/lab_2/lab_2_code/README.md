# Lab 2: Hadoop

## 1. Generate Data

- Run: `$ python3 generate.py <number of lines>`
  - e.g. `python3 generate.py 100`
- Python module: `names`, `random`
- Input: None
- Output: create directory `data/` and generate `grades_100.csv`
  - Format: `<name>,<studentID>,<grade>`
  - e.g. `Michael Huang,0123456789,90`

## 2. Mapper

- Run: `$ ./mapper.sh < data/grades_#.csv`
- Usage: Reads `stdin` with name, studentID and grades separated by newline. Returns the tab-separated pair: `studentID<TAB>grade`
- Input: `stdin` (e.g `Michael Huang,0123456789,100`)
- Output: `stdout` (e.g `0123456789<TAB>10`)
- Test: Use input redirection to read from file `grades.csv`

## 3. Reducer

- Run: `$ ./reducer.sh < data/reducer.in`
- Usage: Reads pairs from the standard input. Each tab-separated pair is composed of a studentID and a list of grades. Returns the max grade for each student on the standard output.
- Input: `stdin` (e.g. `0123456789<TAB>86 100 92`)
- Output: ID and a single number as the max grade (e.g. `0123456789 100`)

## 4. Single Task

- Run

## 5. Hadoop Cluster

### a. HDFS

```bash
hdfs dfs -ls <dir_in_hdfs>
hdfs dfs -mkdir <dir_in_hdfs>
hdfs dfs -put <file_in_your_system> <dir_in_hdfs>
hdfs dfs -get <file_in_hdfs>
hdfs dfs -rm -r -f output
```

You can check via Utilities->Browse file system in `localhost:9870` to check the directory and files on the hdfs.

### b. Streaming

In your hadoop home directory, run streaming with package: `share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar` via the following command after you have created directory in `hdfs` for `<DFS_INPUT_DIR>` and `<DFS_OUTPUT_DIR>`

```bash
hadoop jar <HADOOP_HOME>/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -input <DFS_INPUT_DIR> -output <DFS_OUTPUT_DIR> -mapper <MAPPER> -reducer <REDUCER> -file <LOCAL_MAPPER_DIR>  -file <LOCAL_REDUCER_DIR>
```

*Note*:

- <MAPPER> and <REDUCER> can be local files, while <DFS_INPUT_DIR> and <DFS_OUTPUT_DIR> is in `hdfs`
- `<DFS_OUTPUT_DIR>` needs to be emptyed everytime re-running the mapreduce task

*Error Handling*:

- Check `<HADOOP_HOME>/logs` for detailed logs
- `WARN org.apache.hadoop.streaming.PipeMapRed: java.io.IOException`
  - Check if `#!/usr/bin/env python` is included if you are using `python`
  - Check if shell scripts are granted permission to execute
  - Check if shell scripts handle the exception correctly
