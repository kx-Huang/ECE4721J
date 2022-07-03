ALTER SESSION
SET `store.format` = 'csv';

CREATE TABLE dfs.tmp.variation AS
SELECT country.c_continent AS continent,
    SUBSTR(weather.w_date, 5, 2) AS month,
    AVG(CAST(weather.w_value AS FLOAT)) AS temperature
FROM weather
    INNER JOIN country ON SUBSTR(weather.w_station, 1, 2) = country.c_fips
GROUP BY country.c_continent, month
ORDER BY country.c_continent, month;
