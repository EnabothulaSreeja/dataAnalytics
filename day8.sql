use DataRevature;
select * from Emp;
-- subquery
select ename from Emp where salary<(select avg(salary) from Emp);
select ename, salary from Emp where salary>(select avg(salary) from Emp);
-- create dep table
CREATE TABLE departments1 (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
CREATE TABLE employees2 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
INSERT INTO departments1 (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'HR');
INSERT INTO employees2 (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);
select*from employees2
where department_id in(
	select department_id from departments
    where department_name='Sales'
);

select employee_name,(select department_name from departments1 where departments1.department_id = employees2.department_id) as department_name from employees2;

select employee_name from employees2 where department_id in
 (select department_id from employees2 group by department_id having count(*)>1);
 
select * from departments d where exists
 (select 1 from employees1 e where e.department_id = d.department_id);
 
select department_name from departments d where not exists
 (select 1 from employees1 e where e.department_id = d.department_id);
 
select department_id from employees1 group by department_id having avg(employee_id)>102;

 -- scalar functions operate a single value and return a single value.
 
 select ucase("hello world") as uppercase_string;
 
 select lcase("Hello World") as lowercase_string;
 
 select mid("hello world",4,8) as substring;
 
 select length("hello sreeja") as string_length;
 
 select round(1560.4456,2) as round_value;
 
 select now() as currentdatetime;
 
 select format(1234.1234,2) as format_number;
 
 select employee_name,length(employee_name) as name_length from employees2;
 
 select ProductId,price,round(price) as rounded_price from products; 
 
 -- auto increment / sequence 

 create table users1(
	user_id int auto_increment,
    name varchar(100),
    primary key(user_id)
 );
 
 alter table users1 auto_increment=1001;
 
 select * from users1;
  -- create SEQUENCE example_1
 -- as int start with 10 incerment by 10;
 
 select id, name , coalesce(coupon_code,'default') as applied_coupon from employees;
 
 -- commit - saves the changes of a successful transaction
 -- savepoint - seta a point within a transaction to which you can later rollback if needed, without rolling back
 -- rollback - used to undo the changes done by the transaction

start transaction;
savepoint point2; 
insert into products values ( 4 ,'honda',50000);
insert into products values ( 5 ,'activa',45000);
rollback to point2;
select * from products;
commit;

delimiter //
create procedure GetAllUSERS()
begin
	select * from users;
end;
//
call GetAllUSERS()

delimiter //
create procedure GetUserDetails(IN userID INT)
begin 
	select customer_id,name
    from customers
    where customer_id = userID;
end //
delimiter ;
call GetUserDetails(3);

select * from customers;
insert into customers values(3,'navya');

DELIMITER //
CREATE PROCEDURE GetUserName (IN id INT, OUT name VARCHAR(100))
BEGIN
    SELECT username INTO name
    FROM Users
    WHERE userid = id;
END //
DELIMITER ;

SET @user_name = '';
CALL GetUserName(1, @user_name);
SELECT @user_name;

drop procedure GetUserName;

select * from Users;

create table Users(
	userid int auto_increment primary key,
    username varchar(50) unique not null,
    Email varchar(100) unique not null,
    PasswordHash varchar(150) not null,
    FirstName varchar(50),
    LastName varchar(50),
    DateOfBirth date,
    CreatedAt datetime default current_timestamp,      -- date the user was created, defaults to current time       
    LastLogin datetime,                               -- Last login timestamp
    Status enum('Active','Inactive','Suspended') default 'Active',      -- status of the account
    Index (Email)                     -- Index on the email column to speed up searches       
);
 
insert into Users values(1,'sreeja5','sreeja@example.com','sreeja@123','sreeja','enabothula','2002-09-15',now(),now(),'Active');


