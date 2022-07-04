# ECE4721J: Project 1

Big data analysis on [Million Song Dataset (MSD)](http://millionsongdataset.com)

Goals:
- Work with Hadoop, Drill and Spark
- Compare MapReduce and Spark
- Perform advanced data analysis on big data
- Develop presentations skills (slides + poster)

Team members:
- Yiding Chang
- Yifan Shen
- Kexuan Huang
- Qinhang Wu

## Milestone 0: Compact and Convert

1. Compact small `hdf5` files into larger ones
2. Read `hdf5` file and extract the information
3. Convert `hdf5` file to `Avro` file with `Apache Avro™`

## Milestone 1: Database Queries

1. Find the range of dates covered by the songs in the dataset, i.e. the age of the oldest and of the youngest songs
2. Find the hottest song that is the shortest and shows highest energy with lowest tempo
3. Find the name of the album with the most tracks
4. Find the name of the band who recorded the longest song

## Milestone 2: More Advanced Data Analysis

1. Determine distance between artists with adjacency matrix, using parallelized BFS
2. Propose similar songs with distance and "provide more diverse recommendations"
3. Do it in both MapReduce and Spark to compare the time
4. Prepare a set of slides with Beamer and a poster with Beamerposter for presentations
