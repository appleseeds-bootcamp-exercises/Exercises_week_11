use employees;
show tables;
select * from current_dept_emp;


select year(hire_date) as y, count(*) from employees group by y order by y;
SELECT 
    YEAR(hire_date), MONTH(hire_date), COUNT(*)
FROM
    employees AS e
GROUP BY MONTH(e.hire_date) , YEAR(e.hire_date)
ORDER BY hire_date ASC;


select  emp_no as e, avg(salary) from salaries group by e;
select count(distinct title) from titles;
select title, count(*) from titles group by title;
select  emp_no as e, sum(salary) from salaries group by e;
select count(dept_no) as d from dept_emp group by emp_no order by d desc limit 1;


-- select count(*) from dept_emp where year(hire_date) >  group by dept_no, year(hire_date)
-- select count(*),  year(hire_date) from employees group by year(hire_date);
-- distinct month(hire_date),


-- 1. What is the number of employees hired each year?
-- 2. What is the number of employees hired each month per each year?
-- 3. How many employees were in each department per year?
-- 4. What is the average salary each employee had in their time working for the company?
-- 5. How many different titles are there in the company?
-- 6. How many people hold every different title?
-- 7. How much money did every employee make in the company?
-- 8. What is the maximum amount of departments a single employee worked at?
-- 9. How many male/female employees were there in the company?
-- 10. Who are the 10 youngest employees in the company?