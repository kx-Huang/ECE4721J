#!/bin/sh

for artist in `shuf -n 5 artists`
do
    echo "Searching for "$artist
    start=$SECONDS
    hdfs dfs -rm -r -f /yiding/$artist
    hdfs dfs -mkdir /yiding/$artist

    bash driver.sh /yiding/$artist $artist quiet > $artist.log

    duration = $((SECONDS - start))
    echo "Time for MapReduce is $duration s"
done
