CREATE TABLE name_profession (
    nconst varchar(10) not null,
    profession text not null,
    foreign key(nconst) references name(nconst)
);

create table title_genre (
    tconst varchar(10) not null,
    genre text not null,
    foreign key(tconst) references title(tconst)
);
