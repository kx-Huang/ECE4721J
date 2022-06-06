create table name (
    nconst varchar(10) not null primary key,
    primaryName text not null,
    birthYear varchar(4) not null,
    deathYear varchar(4),
    primaryProfession text not null,
    knownForTitles text not null
);

create table title (
    tconst varchar(10) not null primary key,
    titleType varchar(64) not null,
    primaryTitle text not null,
    originalTitle text not null,
    isAdult boolean not null,
    startYear varchar(4) not null,
    endYear varchar(4),
    runtimeMinutes integer not null,
    genres text not null
);

create table principal (
    tconst varchar(10) not null,
    ordering integer not null,
    nconst varchar(10) not null,
    category text not null,
    job text,
    characters text
);

create table rating (
    tconst varchar(10) not null primary key,
    averageRating double not null,
    numVotes integer not null
);
