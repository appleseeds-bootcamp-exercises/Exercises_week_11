select full_name from actors order by full_name asc;
select count(*) from movies;
select count(*) from movies where genre = 'action';
select count(*) from movies where not genre = 'action';
select year ,count(*) as count from movies group by year order by year asc;
select count(title) from movies where title like '%the%';
select count(title) from movies where title like 'the%';
