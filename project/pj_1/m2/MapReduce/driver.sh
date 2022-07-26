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
    hadoop jar /home/s/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar  -file mapper.py -file reducer.py    -mapper mapper.py  -reducer reducer.py -input $1/output$i/part-00000 -output $1/output$((i + 1)) 
done

# - Getting output
if [ "$3" = "display" ]; then
    echo The similar artists with their distances are
    hdfs dfs -cat $1/output3/part-00000 | grep "|1|\||2|\||3|" | sed "s/|[^0-9].*//"
fi
