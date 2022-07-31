#!/bin/sh
# Usage: bash driver.sh [hdfs working directory] [target] [display]

# - Init graph (need to re-init for every new target)

target=$2
echo Removing existing graph for target $target.
rm input-$target
echo Creating new graph for target $target. This is time consuming.
for artist in `cat artists `
do
    if [ "$artist" = "$target" ]; then
        dist=0
    else
        dist=10000
    fi
echo $artist$artist"||$dist|"$(sqlite3 artist_similarity.db  <<EOF
select * from similarity where target='$artist'
EOF
) | sed "s/$artist|//g" | tr " " "," >> input-$target
done
echo New graph for target $target is in input-$target.

# - BFS Iterations:
echo Preparing the input for BFS Iterations
hdfs dfs -rm -r -f $1/output*
hdfs dfs -mkdir $1/output0
hdfs dfs -put -f input-$target $1/output0/part-00000

for i in {0..2}
do
    echo Starting iteration number $i
    python3 spark.py $1/output$i/part-00000 1>>$1/output$((i + 1)) 2>>$1/output$((i + 1))
done
