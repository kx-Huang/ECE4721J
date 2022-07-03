-- Top 5 stations with highest daily average temperature
SELECT station.s_name AS station,
    weather.w_value AS value
FROM weather
    INNER JOIN station ON station.s_id = weather.w_station
WHERE weather.w_type = 'TAVG'
    AND LENGTH(weather.w_value) > 0
    AND weather.w_value <> -999
ORDER BY CAST(weather.w_value AS INTEGER) DESC
LIMIT 5;

-- Top 5 station with lowest daily minimum temperature on Augest 25, 2017
SELECT station.s_name AS station,
    weather.w_value AS value
FROM weather
    INNER JOIN station ON station.s_id = weather.w_station
WHERE weather.w_type = 'TMIN'
    AND LENGTH(weather.w_value) > 0
    AND weather.w_value <> -999
    AND weather.w_date = '20170825'
ORDER BY CAST(weather.w_value AS INTEGER)
LIMIT 5;

-- Top 5 date with highest average temperature in Shanghai
SELECT country.c_name AS country,
    station.s_name AS station,
    weather.w_date AS day,
    weather.w_value AS value
FROM station
    INNER JOIN country ON SUBSTR(station.s_id, 1, 2) = country.c_fips
    INNER JOIN weather ON station.s_id = weather.w_station
WHERE station.s_name LIKE 'SHANGHAI%'
    AND weather.w_type = 'TAVG'
ORDER BY CAST(weather.w_value AS INTEGER) DESC
LIMIT 5;
