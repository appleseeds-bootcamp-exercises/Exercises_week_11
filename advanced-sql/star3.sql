use employees;
select first_name name, last_name, from_date from employees e join titles t on e.emp_no = t.emp_no where t.title = 'Assistant Engineer' order by t.from_date asc limit 10;
select first_name name, last_name, from_date from employees e join titles t on e.emp_no = t.emp_no where t.title = 'Senior Engineer' order by t.from_date asc limit 10, 10;
select dept_name, count( distinct e.emp_no) from  titles t  join employees e on e.emp_no=t.emp_no join dept_emp d on e.emp_no=d.emp_no join departments depts on d.dept_no= depts.dept_no where title like '%Engineer%' group by depts.dept_name;
select depts.dept_name, max(s.salary), e.first_name name, e.last_name 'last name' from employees e join salaries s on e.emp_no=s.emp_no join dept_emp d on e.emp_no= d.emp_no join departments depts on d.dept_no=depts.dept_no group by depts.dept_name;
