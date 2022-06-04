#!/bin/bash
# run this script on root@hadoop-master:/home/s/lab2_benchmark
# Structure: /home/s/lab2_benchmark
#                    ├── benchmark.sh
#                    ├── input
#                    │   ├── grades_100000000.csv
#                    │   ├── grades_10000000.csv
#                    │   ├── grades_1000000.csv
#                    │   ├── grades_100000.csv
#                    │   ├── grades_10000.csv
#                    │   └── grades_1000.csv
#                    ├── log
#                    │   └── time.log
#                    └── output
#                        ├── 100000000.out
#                        ├── 10000000.out
#                        ├── 1000000.out
#                        ├── 100000.out
#                        ├── 10000.out
#                        └── 1000.out

mkdir -p output
mkdir -p log

# delete HDFS input/lab2
hdfs dfs -rm -r -f input/lab2

# copy input to HDFS
mv input/ lab2/
hdfs dfs -put lab2/ input/
mv lab2/ input/

rm -f log/time.log

for ((NUM=1000;NUM<=100000000;))
do
    hdfs dfs -rm -r -f output/
    cd /home/s/hadoop

    start=$SECONDS

    hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -input input/lab2/grades_$NUM.csv -output output -mapper /src/mapper.sh -reducer "python reducer.py" -file /src/mapper.sh  -file /src/reducer.py

    end=$SECONDS

    cd /home/s/lab2_benchmark
    hdfs dfs -get output/part-00000
    mv part-00000 output/$NUM.out

    duration=$(($end - $start))
    echo $NUM: $duration >> log/time.log

    ((NUM=$NUM*10))
done
