# Lab 2

## Generate Raw Data

- Run: `.../data $ python generate.py`
- Python module: `names`, `random`
- Input: None
- Ouput: 3 text files
  - `.../data/firstnames.txt`
  - `.../data/lastnames.txt`
  - `.../data/id.txt`

## Generate `grades.csv`

- run: `.../lab_2_code $ ./grading.sh`

## Mapper

- run: `.../lab_2_code $ ./mapper.sh`
- Usage: Reads grades.csv with name, studentID and grades and returns the tab-separated pair: `studentID<TAB>grade`
- Input: `grades.csv` (e.g `Michael Huang,0123456789,100`)
- Output: `stdout` (e.g `0123456789<TAB>10`)

## Reducer

- run: `.../lab_2_code $ ./reducer.sh`
- Usage: Reads pairs from the standard input. Each tab-separated pair is composed of a studentID and a list of grades. Returns the max grade for each student on the standard output.
- Input: `stdin` (e.g. `0123456789<TAB>86 100 92`)
- Output: A single number as the max grade (e.g. `100`)

## Run MapReduce in Hadoop
```bash
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming*.jar -input /input -output /avgwl -mapper mapper.sh -reducer reducer.sh -file /home/user/mr_streaming_bash/mapper.sh -file /home/user/mr_streaming_bash/reducer.sh
```
