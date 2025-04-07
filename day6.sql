create database DataRevature;
use DataRevature;
CREATE TABLE Person(
	PersonID int,
    Lastname varchar(255),
    Firstname varchar(255),
    Address varchar(255),
    city varchar(255)
);
INSERT INTO Person values(1,"sreeja","enabothula","warangal","warangal");
INSERT INTO Person values(2,"ammu","sreeja","hyd","warangal");
select * from Person;
delete from Person where PersonID=1;
update Person set Firstname='ammu' where PersonID=2;


create table Users(
	UserID int auto_increment primary key,
    Username varchar(50) unique not null,
    email varchar(50) unique not null,
    passwordHash varchar(255) not null,
    firstname varchar(50),
    lastname varchar(50),
    dateofbirth date,
    createdAt datetime default current_timestamp,
    lastlogin datetime,
    status enum('active','inactive','suspended')default 'active',
    index(email)
);
insert into Users values(1,"sreeja","sreeja@gmail.com","12345","sreeja","enabothula","02-06-24",now(),now(),"active")
select * from Users;

create table stud(
	stud_id int primary key,
    name varchar(100),
    age int,
    check(age>18)
);

create table enrollments(
	enrollments_id int primary key,
    stud_id int,
    course_id int,
    foreign key(stud_id) references stud(stud_id)
);

insert into stud values(1,"sreeja",20);
insert into enrollments values(101,1,10);
select * from stud;
select * from enrollments;
create table orderdetails(
	order_id int,
    product_id int,
    quantity int,
    primary key(order_id,product_id)
);
insert into orderdetails values(1,1001,10);
select * from orderdetails;
drop table Users;
truncate table Users;
desc Users;