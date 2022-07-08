-- Age of the oldest songs
SELECT 2022 - MAX(Year) AS Age
FROM hdfs.`/pj_1/m0/output.avro`;

-- Age of the youngest songs
SELECT 2022 - MIN(Year) As Age
FROM hdfs.`/pj_1/m0/output.avro`
WHERE YEAR > 0;

-- The hottest song that is the shortest and shows highest energy with lowest tempo
SELECT song_id,
    title
FROM hdfs.`/pj_1/m0/output.avro`
WHERE song_hotttnesss <> 'NaN'
ORDER BY song_hotttnesss DESC,
    duration ASC,
    energy DESC,
    tempo ASC
LIMIT 10;

-- Find the name of the album with the most tracks
SELECT release,
    COUNT(release) AS NumTrack
from hdfs.`/pj_1/m0/output.avro`
GROUP BY release
ORDER BY NumTrack desc
LIMIT 1;

-- The name of the band who recorded the longest song
SELECT artist_name,
    duration
from hdfs.`/pj_1/m0/output.avro`
ORDER BY duration DESC
LIMIT 1;
