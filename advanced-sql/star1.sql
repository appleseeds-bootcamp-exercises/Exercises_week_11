create database programs;
use programs;

CREATE TABLE participant (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    country VARCHAR(15),
    gender ENUM('M', 'F'),
    level_of_english ENUM('bad', 'ok', 'good'),
    israei_citizenship BOOLEAN,
    GPA FLOAT
);

CREATE TABLE payment (
    payment_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    participant_id INT NOT NULL,
    sum INT NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('paypal', 'cash'),
    authorization_code VARCHAR(40) NOT NULL,
    FOREIGN KEY (participant_id)
        REFERENCES participant (id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

insert into participant
values(null, 'Dave', 'Manu', 'angola', 'F', 'ok', true, 59.6),
(null, 'Gilad', 'Leslau', 'US', 'M', 'good', false, 93.7);

insert into payment
values(null, 2, 3000, default, 'paypal', 'thdasfefqe324ere'),
(null, 1,2500,default, 'cash', 'r32ty43dewf');


insert into payment
values(1, 2, 3000, default, 'paypal', 'thdasfefqe324ere');
