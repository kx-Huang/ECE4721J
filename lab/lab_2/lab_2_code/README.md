# Lab 2: Hadoop

## Generate Data

- run: `.../lab_2_code $ python3 generate.py <number of lines>`
  - e.g. `python3 generate.py 100`
- Python module: `names`, `random`
- Input: None
- output: create directory `data/` and generate `grades_100.csv`
  - format: `<name>,<studentID>,<grade>`
  - e.g. `Michael Huang,0123456789,90`

## Mapper

- run: `.../lab_2_code $ ./mapper.sh < data/grades_#.csv`
- Usage: Reads `stdin` with name, studentID and grades separated by newline. Returns the tab-separated pair: `studentID<TAB>grade`
- Input: `stdin` (e.g `Michael Huang,0123456789,100`)
- Output: `stdout` (e.g `0123456789<TAB>10`)
- Test: Use input redirection to read from file `grades.csv`

## Reducer

- run: `.../lab_2_code $ ./reducer.sh < data/reducer.in`
- Usage: Reads pairs from the standard input. Each tab-separated pair is composed of a studentID and a list of grades. Returns the max grade for each student on the standard output.
- Input: `stdin` (e.g. `0123456789<TAB>86 100 92`)
- Output: A single number as the max grade (e.g. `100`)
- Test: Use input redirection to read from file `data/reducer.in`

## Hadoop Pseudo Distribution

### HDFS

```bash
hdfs dfs -ls <dir_in_hdfs>
hdfs dfs -mkdir <dir_in_hdfs>
hdfs dfs -put <file_in_your_system> <dir_in_hdfs>
hdfs dfs -get <file_in_hdfs>
hdfs dfs -rm -r -f output/ # need to empty the output directory everytime rerunning the code
```

You can check via Utilities->Browse file system in `localhost:9870` to check the directory and files on the hdfs.

### Streaming

- In your hadoop home directory, run streaming with package: `share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar` via the following command after you have created `dir_in_hdfs` for `inputdir` and `outputdir`.

```bash
hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -input inputdir -output outputdir -mapper mapper.sh -reducer reducer.sh -file localdirectorymapper.sh  -file localdirectoryreducer.sh
```

- Note: `reducer.sh` and `mapper.sh` can be local file, while inputfile is in the HDFS
