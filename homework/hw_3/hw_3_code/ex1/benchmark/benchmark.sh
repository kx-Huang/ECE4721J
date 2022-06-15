#!/bin/bash
# run this script on root@hadoop-master:/home/s/kexuan/h3e1
# Structure: h3e1
#            ├── benchmark.sh
#            ├── input
#            │   ├── grades_100000000.csv
#            │   ├── grades_10000000.csv
#            │   ├── grades_1000000.csv
#            │   ├── grades_100000.csv
#            │   ├── grades_10000.csv
#            │   └── grades_1000.csv
#            ├── log
#            │   └── time.log
#            └── output
#                ├── 100000000.out
#                ├── 10000000.out
#                ├── 1000000.out
#                ├── 100000.out
#                ├── 10000.out
#                └── 1000.out

# change working directory to project directory
cd ..

# compile java source file
mvn package

# create folder for output and log
mkdir -p output
mkdir -p log

# delete HDFS input/lab2
hdfs dfs -rm -r -f /kexuan/h3e1/input
hdfs dfs -rm -r -f /kexuan/h3e1/output

# delete last log
rm -f log/time.log

# run mapreduce for each input file
for ((NUM=1000;NUM<=100000000;))
do
    # copy input to HDFS
    hdfs dfs -put input/grades_$NUM.csv /kexuan/h3e1/input

    # remove output folder in HDFS
    hdfs dfs -rm -r -f /kexuan/h3e1/output

    # run mapreduce task
    start=$SECONDS # start counting time
	hadoop jar target/ex1-1.0-SNAPSHOT.jar /kexuan/h3e1/input /kexuan/h3e1/output
    end=$SECONDS # end counting time

    # calculate time elapsed and save to log
    duration=$(($end - $start))
    echo $NUM: $duration >> log/time.log

    # copy output from HDFS to local
    hdfs dfs -get /kexuan/h3e1/output/part-r-00000
    mv part-r-00000 output/$NUM.out

    # next file size
    ((NUM=$NUM*10))
done
