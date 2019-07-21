select * from actors where full_name like '%Dan%';
select * from actors where full_name like 'Ben%' and gender = 'M';
select salary from cast order by salary asc limit 5;