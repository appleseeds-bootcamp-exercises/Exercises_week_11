SELECT 
    YEAR(hire_date) AS y, COUNT(*)
FROM
    employees
GROUP BY y
ORDER BY y;


SELECT 
    YEAR(hire_date), MONTH(hire_date), COUNT(*)
FROM
    employees AS e
GROUP BY MONTH(e.hire_date) , YEAR(e.hire_date)
ORDER BY hire_date ASC;


SELECT 
    dept_no, COUNT(emp_no)
FROM
    dept_emp
GROUP BY dept_no;


SELECT 
    emp_no AS e, AVG(salary)
FROM
    salaries
GROUP BY e;


SELECT 
    COUNT(DISTINCT title)
FROM
    titles;
    
    
SELECT 
    title, COUNT(*)
FROM
    titles
GROUP BY title;


SELECT 
    emp_no AS e, SUM(salary)
FROM
    salaries
GROUP BY e;


SELECT 
    COUNT(dept_no) AS d
FROM
    dept_emp
GROUP BY emp_no
ORDER BY d DESC
LIMIT 1;


SELECT 
    gender, COUNT(*)
FROM
    employees
GROUP BY gender;


SELECT 
    emp_no, birth_date
FROM
    employees
ORDER BY birth_date DESC
LIMIT 10;