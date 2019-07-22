use employees;	
SELECT 
    gender, COUNT(*)
FROM
    employees
GROUP BY gender;

SELECT 
    COUNT(DISTINCT title)
FROM
    titles;
    
SELECT 
    first_name, last_name, title
FROM
    employees AS e
        JOIN
    titles AS t
WHERE
    YEAR(e.hire_date) = 1993;
 
 
SELECT 
    *
FROM
    employees AS e
        JOIN
    titles AS t ON e.emp_no = t.emp_no
        JOIN
    salaries AS s ON e.emp_no = s.emp_no
WHERE
    t.title = 'staff'
ORDER BY s.salary ASC
LIMIT 10;

SELECT 
    title, AVG(salary) avag
FROM
    salaries s
        JOIN
    titles t ON s.emp_no = t.emp_no
GROUP BY title
ORDER BY avag DESC;