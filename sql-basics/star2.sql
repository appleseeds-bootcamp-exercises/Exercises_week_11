CREATE DATABASE bootcamp;
use bootcamp;
CREATE TABLE students(
student_id INT auto_increment primary key,
first_name VARCHAR(30),
last_name VARCHAR(30),
been_dismissed VARCHAR(15),
cohort varchar(20)
);

CREATE TABLE grades(
student_id INT,
exam_id int auto_increment primary key,
date_taken Date,
grade tinyint
);

insert into students (first_name, last_name, been_dismissed, cohort) values
('David', 'Beckham','yes', '2019 A'),
('Sapir', 'Bessckham','no', '2017 B'),
('Elchai', 'Hachi Tov','yes', '2010 AA');
update students set first_name = 'Shlomo' where student_id = 1;
delete from students where student_id = 2;


