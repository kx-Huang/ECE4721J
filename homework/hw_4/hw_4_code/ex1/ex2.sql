SELECT DISTINCT(country.c_name) AS country,
    country.c_continent AS continent
FROM station
    INNER JOIN country ON SUBSTR(station.s_id, 1, 2) = country.c_fips
    INNER JOIN weather ON station.s_id = weather.w_station
WHERE (
        weather.w_date > 20170701
        AND weather.w_date < 20170831
        AND (
            weather.w_type = 'TAVG'
            AND CAST(weather.w_value AS FLOAT) > 150
            AND CAST(weather.w_value AS FLOAT) < 300
        )
        OR (
            weather.w_type = 'TMAX'
            AND CAST(weather.w_value AS FLOAT) < 30
        )
        OR (
            weather.w_type = 'TIN'
            AND CAST(weather.w_value AS FLOAT) > 10
        )
        OR (
            weather.w_type = 'PRCP'
            AND CAST(weather.w_value AS FLOAT) > 10
            AND CAST(weather.w_value AS FLOAT) < 20
        )
    )
LIMIT 5;