#!/usr/bin/python3
import sqlite3

# connect to sqlite3 database
conn = sqlite3.connect('var/imdb.sqlite3')
c = conn.cursor()

# get nscont-profession pair from name table
insert_list = []
entries = c.execute("select * from name")
for entry in entries:
    if entry[4] != '\\N' and len(entry[4]) > 0:
        nconst = entry[0]
        professions = entry[4].split(',')
        for profession in professions:
            insert_list.append((nconst, profession))

# insert nscont-profession pair in the list into the name_profession table
c.executemany("insert into name_profession values (?,?)", insert_list)

# get nscont-profession pair from name table
insert_list = []
entries = c.execute("select * from title")
for entry in entries:
    if entry[8] != '\\N' and len(entry[8])>0:
        tconst = entry[0]
        genres = entry[8].split(',')
        for genre in genres:
            insert_list.append((tconst,genre))

# insert tscont-genre pair in the list into the title_genre table
c.executemany("insert into title_genre values (?,?)",insert_list)

# Save (commit) the changes
conn.commit()

# clse the connection
conn.close()
