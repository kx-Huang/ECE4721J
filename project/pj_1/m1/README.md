# Project 1 Milestone 1: Drill Database Query

Query [Million Song Dataset (MSD)](http://millionsongdataset.com) with `Drill`:

1. Find the range of dates covered by the songs in the dataset, i.e. the age of the oldest and of the youngest songs
2. Find the hottest song that is the shortest and shows highest energy with lowest tempo
3. Find the name of the album with the most tracks
4. Find the name of the band who recorded the longest song

## 1. The range of dates covered by the songs in the dataset

- SQL

    ```sql
    -- Age of the oldest songs
    SELECT 2022 - MAX(year) AS Age
    FROM hdfs.`/pj/m0/output.avro`;

    -- Age of the youngest songs
    SELECT 2022 - MIN(year) AS Age
    FROM hdfs.`/pj/m0/output.avro`
    WHERE year > 0;
    ```

- Result

    ```log
    +--------+
    |  Age   |
    +--------+
    | 12     |
    +--------+
    1 row selected (8.864 seconds)

    +--------+
    |  Age   |
    +--------+
    | 96     |
    +--------+
    1 row selected (0.642 seconds)
    ```

Therefore, the age of the oldest song is 96 and the age of the youngest is 12, so the range of dates covered by the songs in the dataset is 84 years.

## 2. The hottest song that is the shortest and shows highest energy with lowest tempo

As the query will return 5648 result, we just return the first 10 records.

- SQL

    ```sql
    SELECT song_id,
        title
    FROM hdfs.`/pj/m0/output.avro`
    WHERE song_hotttnesss <> 'NaN'
    ORDER BY song_hotttnesss DESC,
        duration ASC,
        energy DESC,
        tempo ASC
    LIMIT 10;
    ```

- Result

    ```log
    +-----------------------+------------------------------------------------------+
    |        song_id        |                        title                         |
    +-----------------------+------------------------------------------------------+
    | b'SOAAXAK12A8C13C030' | b'Immigrant Song (Album Version)'                    |
    | b'SOULTKQ12AB018A183' | b"Nothin' On You [feat. Bruno Mars] (Album Version)" |
    | b'SOTRSHW12A58A79E7C' | b'This Christmas (LP Version)'                       |
    | b'SOWFUUS12AB01800E7' | b'If Today Was Your Last Day (Album Version)'        |
    | b'SOOXLKF12A6D4F594A' | b'Harder To Breathe'                                 |
    | b'SOMKGQN12A8C1339D2' | b'Blue Orchid'                                       |
    | b'SOOPVJI12AB0183957' | b'Just Say Yes'                                      |
    | b'SOUXEOI12A6D4FB18E' | b'They Reminisce Over You (Single Version)'          |
    | b'SOBVAPJ12AB018739D' | b'Exogenesis: Symphony Part 1 [Overture]'            |
    | b'SOFDYGC12A6D4F9059' | b'Inertiatic Esp'                                    |
    +-----------------------+------------------------------------------------------+
    10 rows selected (0.471 seconds)
    ```

## 3. The name of the album with the most tracks

- SQL

    ```sql
    SELECT release,
        COUNT(release) AS NumTrack
    FROM hdfs.`/pj/m0/output.avro`
    GROUP BY release
    ORDER BY NumTrack desc
    LIMIT 1;
    ```

- Result

    ```log
    +------------------+----------+
    |     release      | NumTrack |
    +------------------+----------+
    | b'Greatest Hits' | 21       |
    +------------------+----------+
    1 row selected (0.695 seconds)
    ```

## 4. The name of the band who recorded the longest song

- SQL

    ```sql
    SELECT artist_name,
        duration
    FROM hdfs.`/pj/m0/output.avro`
    ORDER BY duration DESC
    LIMIT 1;
    ```

- Result

    ```log
    +-------------+-----------+
    | artist_name | duration  |
    +-------------+-----------+
    | b'UFO'      | 1819.7677 |
    +-------------+-----------+
    1 row selected (0.27 seconds)
    ```
