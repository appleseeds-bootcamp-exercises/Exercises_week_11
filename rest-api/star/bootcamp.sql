CREATE database bootcamp;
use bootcamp;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(20) UNIQUE,
    is_cute BOOLEAN
);
CREATE TABLE cohorts (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(20) UNIQUE
);