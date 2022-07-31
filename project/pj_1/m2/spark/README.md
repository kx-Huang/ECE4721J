# BFS with Spark

## Preparation

BFS with Spark is implemented in python with several additional packages required. Use the command to install them first:
`pip3 install pyspark mrjob`

## Run MapReduce on Spark

Similarily with the mapReduce part, we run BFS with spark on the millionsongdataset that searches for similar artists with a distance of 3. We assume that the database and the queries are ready as is indicated in mapReduce part. Then we run

```bash
$ bash bench.sh
```
to start the benchmark. We can also run

```bash
$ time python3 spark.py [inputGraphFile]
```
to start a local test.
