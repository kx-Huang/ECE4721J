-- Determine the name of the student who had the lowest grade
SELECT name,
    MIN(CAST(score AS INTEGER)) AS minScore
FROM (
        SELECT COLUMNS [0] AS name,
            COLUMNS [2] AS score
        FROM hdfs.root.`/user/root/input/grades_200000000.csv`
    )
GROUP BY name
ORDER BY minScore
LIMIT 1;

-- Determine the name of the student who had the highest average score
SELECT name,
    AVG(CAST(score AS INTEGER)) AS avgScore
FROM (
        SELECT COLUMNS [0] AS name,
            COLUMNS [2] AS score
        FROM hdfs.root.`/user/root/input/grades_200000000.csv`
    )
GROUP BY name
ORDER BY avgScore DESC
LIMIT 1;

-- Calculate the median over all the scores
SELECT AVG(CAST(score AS INTEGER))
FROM (
        SELECT COLUMNS [2] AS score
        FROM hdfs.root.`/user/root/input/grades_200000000.csv`
    )
ORDER BY score
LIMIT 2 OFFSET 99999999;
