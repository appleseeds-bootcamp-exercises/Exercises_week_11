use employees;
SELECT 
    depts.dept_name, first_name name, last_name 'last name'
FROM
    dept_manager d
        JOIN
    employees e ON e.emp_no = d.emp_no
        JOIN
    departments depts ON depts.dept_no = d.dept_no
ORDER BY DATEDIFF(to_date, from_date) DESC
LIMIT 1;
SELECT 
    gender, dept_name, COUNT(*)
FROM
    employees e
        JOIN
    dept_emp d ON e.emp_no = d.emp_no
        JOIN
    departments depts ON depts.dept_no = d.dept_no
WHERE
    YEAR(hire_date) <= 1995
GROUP BY gender , depts.dept_name;
