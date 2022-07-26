# BFS with MapReduce

## Functionalities

Runs BFS on the [MillionSongDataset](http://millionsongdataset.com/) to search for similar artists to a certain artist within distance 3. The BFS part is done with MapReduce, but neither the generation of the graph or the retrieval of the results is done with MapReduce, albeit doable. This is to keep consistency with the Spark version.

## Preparation

- Prerequisites: Hadoop, python3, sqlite3

- Similarity among artists is acquired from http://www.ee.columbia.edu/~thierry/artist_similarity.db. Put it in the working directory and get a list of the artists in a file called `artists` first:

    ``` bash
    wget http://www.ee.columbia.edu/~thierry/artist_similarity.db
    sqlite3 artist_similarity.db > artists <<EOF
    SELECT * FROM artists
    EOF
    ```

## Running

Run from the directory where `mapper.py` and `reducer.py` can be found, with the following command:

```bash
$ bash driver.sh [hdfs working directory] [target artist] [display]
```

*NOTE*: if your working directory has sub-directories with names like `outputN` where `N` is a number, they WILL get OVERWRITTEN)

where:
- `hdfs working directory` is where you want the data and results to be on hdfs;
- `target artist` is the `artistID` of the source artist. Find the `artistID` from the generated `artists` file;
- `display` takes either "display" or "quiet" as an argument, the former displaying the recommended artists, and the latter not.

e.g:

``` bash
$ bash driver.sh /yiding AR002UA1187B9A637D display
```

## Benchmarking

Run benchmark with:

```bash
$ bash bench.sh
```

Sample benchmarking results can be found in `benchresults`. The results are run on an SJTU cluster with three machines. Each machine has a Dualcore Intel Xeon Processor (Skylake, IBRS) and 4GB of memory.
