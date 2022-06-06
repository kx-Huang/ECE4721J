# Lab 3: SQLite

## 0. Create SQLitie Database

```bash
$ mkdir var
$ sqlite3 var/imdb.sqlite3
sqlite> .quit
```

## 1. Import the Data

1. Remove the first line (header) of the TSV files

    ```bash
    $ chmod +x remove.sh
    $ ./remove.sh
    ```

2. Create data schema

    ```bash
    $ sqlite3 var/imdb.sqlite3 < schema_ex3.sql
    $ sqlite3 var/imdb.sqlite3 < schema_ex5.sql
    ```

3. Import TSV file to create table

    ```bash
    $ sqlite3 var/imdb.sqlite3 < import.sql
    ```

## 2. Execute Query

```bash
$ sqlite3 var/imdb.sqlite3 < query_ex3.sql > query_ex3.out
$ sqlite3 var/imdb.sqlite3 < query_ex5.sql > query_ex5.out
```

## 3. Interaction with SQLite using Python

Split `primaryProfession` from `name` table into `nscont-profession` pair and insert them into the `name_profession` table

```bash
python insert.py
```
