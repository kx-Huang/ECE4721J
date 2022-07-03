# Homework 4

## 0. Setup the schema

### 0.1 Weather

```sql
CREATE TABLE dfs.tmp.`weather` AS
SELECT *
FROM (
        SELECT columns[0] AS w_station,
            columns[1] AS w_date,
            columns[2] AS w_type,
            columns[3] AS w_value
        FROM dfs.`/data/2017.csv`
    );
```

### 0.2 Country

```sql
CREATE TABLE dfs.tmp.`country` AS
SELECT *
FROM (
        SELECT columns[0] AS c_name,
            columns[1] AS c_continent,
            columns[2] AS c_fips
        FROM dfs.`/data/country_continent.csv`
    );
```
### 0.3 Station

```sql
CREATE TABLE dfs.tmp.`station` AS
SELECT *
FROM (
        SELECT TRIM(SUBSTR(columns[0], 1, 11)) AS s_id,
            TRIM(SUBSTR(columns[0], 13, 8)) AS s_latitude,
            TRIM(SUBSTR(columns[0], 22, 9)) AS s_longitude,
            TRIM(SUBSTR(columns[0], 32, 6)) AS s_altitude,
            TRIM(SUBSTR(columns[0], 39, 2)) AS s_state,
            TRIM(SUBSTR(columns[0], 42, 30)) AS s_name
        FROM dfs.`/Users/michaelhuang/Desktop/ECE4721J/homework/hw_4/hw_4_code/ex1/meta.csv`
    );
```

## Change path

```sql
USE dfs.tmp
```

## Change output format

```sql
ALTER SESSION
SET `store.format` = 'csv';
```
