# Lab 2: Hadoop Cluster Benchmark

## Run Haddop Mapreduce Tasks
- Path:  `root@hadoop-master:/home/s/lab2_benchmark`
- Stucture:

  ```log
  /home/s/lab2_benchmark
          ├── benchmark.sh
          ├── input
          │   ├── grades_100000000.csv
          │   ├── grades_10000000.csv
          │   ├── grades_1000000.csv
          │   ├── grades_100000.csv
          │   ├── grades_10000.csv
          │   └── grades_1000.csv
          ├── log
          │   └── time.log
          └── output
              ├── 100000000.out
              ├── 10000000.out
              ├── 1000000.out
              ├── 100000.out
              ├── 10000.out
              └── 1000.out
  ```

- Command

  ```bash
  $ chmod +x ./benchmark.sh
  $ ./benchmark.sh
  ```

- Remark: make sure mapper and reducer source files are put to HDFS in `/src/`, e.g. `hdfs dfs -put ../mapper.sh /src/`
- Input: put `grades_<NUM>.csv` into local folder `input/`
- Output: `/log/time.log` containing task time in seconds in local folder `output`
- Effect:
  1. copy the CSV files in local folder `input/` to HDFS
  2. For each file in local folder `input/`:
     - run mapreduce tasks
     - calculate time used in seconds
  3. Generate a log file `time.log` in local folder `log/`

## Scatter and fitting Plot

- Run: `$ python3 plot.py`
- Ouput: plots saved to local folder `img/`
