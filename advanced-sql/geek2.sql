SELECT 
    first_name, last_name, MIN(salary)
FROM
    titles t
        JOIN
    employees e ON e.emp_no = t.emp_no
        JOIN
    salaries s ON s.emp_no = e.emp_no
WHERE
    title = 'staff'
GROUP BY e.emp_no
ORDER BY MIN(salary) ASC
LIMIT 10;

SELECT 
    first_name, last_name, MIN(salary)
FROM
    titles t
        JOIN
    employees e ON e.emp_no = t.emp_no
        JOIN
    salaries s ON s.emp_no = e.emp_no
WHERE
    title = 'Assistant Engineer'
        AND salary > 40000
GROUP BY e.emp_no
ORDER BY MIN(salary) ASC
LIMIT 10;

SELECT 
    first_name, last_name, MIN(salary)
FROM
    titles t
        JOIN
    employees e ON e.emp_no = t.emp_no
        JOIN
    salaries s ON s.emp_no = e.emp_no
            JOIN
    dept_emp d ON d.emp_no = e.emp_no
            JOIN
    departments depts ON depts.dept_no = d.dept_no
WHERE
    title = 'Assistant Engineer'
        AND salary > 40000
        and d.to_date = '9999-01-01'
GROUP BY e.emp_no
ORDER BY MIN(salary) ASC
LIMIT 10;

SELECT 
    first_name, last_name, depts.dept_name, sub.dept_size
FROM
    dept_manager dm
        JOIN
    employees e ON e.emp_no = dm.emp_no
        JOIN
    departments depts ON dm.dept_no = depts.dept_no
        JOIN
    (SELECT 
        COUNT(*) AS dept_size, dept_no
    FROM
        dept_emp
    WHERE
        to_date = '9999-01-01'
    GROUP BY dept_no) sub ON dm.dept_no = sub.dept_no
WHERE
    dm.to_date = '9999-01-01'
ORDER BY sub.dept_size DESC
LIMIT 1;
