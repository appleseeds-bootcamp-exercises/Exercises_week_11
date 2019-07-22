
use employees;

SELECT 
    first_name name, last_name, from_date
FROM
    employees e
        JOIN
    titles t ON e.emp_no = t.emp_no
WHERE
    t.title = 'Assistant Engineer'
ORDER BY t.from_date ASC
LIMIT 10;

SELECT 
    first_name name, last_name, from_date
FROM
    employees e
        JOIN
    titles t ON e.emp_no = t.emp_no
WHERE
    t.title = 'Senior Engineer'
ORDER BY t.from_date ASC
LIMIT 10 , 10;

SELECT 
    dept_name, COUNT(DISTINCT e.emp_no)
FROM
    titles t
        JOIN
    employees e ON e.emp_no = t.emp_no
        JOIN
    dept_emp d ON e.emp_no = d.emp_no
        JOIN
    departments depts ON d.dept_no = depts.dept_no
WHERE
    title LIKE '%Engineer%'
GROUP BY depts.dept_name;

SELECT 
    depts.dept_name,
    MAX(s.salary),
    e.first_name name,
    e.last_name 'last name'
FROM
    employees e
        JOIN
    salaries s ON e.emp_no = s.emp_no
        JOIN
    dept_emp d ON e.emp_no = d.emp_no
        JOIN
    departments depts ON d.dept_no = depts.dept_no
GROUP BY depts.dept_name;
