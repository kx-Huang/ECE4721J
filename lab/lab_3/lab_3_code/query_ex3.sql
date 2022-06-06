.mode column
.headers on
.separator ROW "\n"
.nullvalue NULL

-- The oldest movie
select primaryTitle,
    startYear
from title
where startYear <> "\N"
    and titleType = "movie"
order by startYear
limit 1;

-- The longest movie in 2009
select primaryTitle,
    runtimeMinutes
from title
where startYear = "2009"
    and runtimeMinutes <> "\N"
    and titleType = "movie"
order by runtimeMinutes desc
limit 1;

-- The year with the most movies
select startYear,
    count(*) as count
from title
where startYear <> "\N"
    and titleType = "movie"
group by startYear
order by count desc
limit 1;

-- The name of the person who contains in the most movies
select name.primaryName,
    count(*) as contained
from name,
    principal,
    title
where principal.tconst = title.tconst
    and principal.nconst = name.nconst
    and title.titleType = "movie"
group by principal.nconst
order by contained desc
limit 1;

-- The principal crew of the movie with highest average ratings and more than 500 votes
select name.primaryName,
    principal.category
from name,
    principal
where name.nconst = principal.nconst
    and principal.tconst in (
        select rating.tconst
        from rating
        where rating.numVotes > 500
        order by rating.averageRating desc
        limit 1
    );

-- The count of each Pair<BirthYear, DeathYear> of the people
select birthYear,
    deathYear,
    count(*) as count
from name
where birthYear <> "\N"
    and deathYear <> "\N"
group by birthYear,
    deathYear
order by count desc;
