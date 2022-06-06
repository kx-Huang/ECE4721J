.mode column
.headers on
.separator ROW "\n"
.nullvalue NULL

-- The top 3 most common professions among these people and also the average life span of these three professions
select profession,
    count(*) as count,
    avg(deathYear - birthYear) as avgLifeSpan
from name,
    name_profession
where name.nconst = name_profession.nconst
    and deathYear <> "\N"
    and birthYear <> "\N" -- group by profession
order by count desc
limit 3;

-- The top 3 most popular (received most votes) genres
select genre,
    sum(numVotes) as votes
from rating,
    title_genre
where rating.tconst = title_genre.tconst
group by genre
order by votes desc
limit 3;

-- The average time span (endYear - startYear) of the titles for each person
select name.primaryName,
    avg(title.endYear - title.startYear) as avgTimeSpan
from principal,
    name,
    title
where title.tconst = principal.tconst
    and name.nconst = principal.nconst
    and title.startYear <> "\N"
    and title.endYear <> "\N"
group by principal.nconst
order by avgTimeSpan desc;
