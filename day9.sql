use DataRevature;
create table emp1(
	emp_id int auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    dep varchar(50),
    salary decimal(10,2),
    hire_date date
);
insert into emp1 values(1,'ram','sree','admine',100000,date '2024-02-12'),(2,'george','sge','manager',200000,date '2024-02-12'),(3,'aravind','dgdf','admine',300000,date '2024-02-1'),(4,'nivetha','dgfh''sales',250000,date '2024-02-02');

create view sales_emp as 
select emp_id, first_name,last_name,salary
from emp1
where dep='sales';
select * from sales_emp;
create or replace view sales_emp as
select emp_id , first_name,last_name,salary,hire_date
from emp1
where dep='sales';
drop view sales_emp;
update sales_emp
set salary = salary *1.10
where emp_id=1;
-- trigger is a database obj that automatically execute a block  of sql
create table items(id int primary key, name varchar(255) not null,price decimal(10,2)not null);
INSERT INTO items(id, name, price) 
VALUES (1, 'Item', 50.00);
update items set name='laptop' where ID=1;

CREATE TABLE item_changes (
    change_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    change_type VARCHAR(10),
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(id)
);

DELIMITER //
create trigger update_items_trigger
after update
on items
for each row
begin
	insert into item_changes(item_id,change_type)
    values(new.id,'update');
end;
//
select*from items;
select *from item_changes;

CREATE TABLE employee1 (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);
 
INSERT INTO employee1 (employee_id, name, department, salary) VALUES
(1, 'Alice',   'Sales', 50000),
(2, 'Bob',     'Sales', 60000),
(3, 'Charlie', 'Sales', 45000),
(4, 'David',   'IT',    70000),
(5, 'Eva',     'IT',    80000),
(6, 'Frank',   'IT',    75000);
-- rank emp by salary within each dep
select 
	employee_id,
    name,
    department,
    salary,
    row_number() over (partition by department order by salary desc) as rank_in_dept
from employee1;

-- running total
select
	employee_id,
    name,
    salary,
    sum(salary) over(order by salary)as running_total
from employee1;
-- compare
select
	employee_id,
    name,
    salary,
    lag(salary) over(order by salary)as previous_salary,
    lead(salary)over(order by salary) as next_salry
from employee1;
-- rank
select
	employee_id,
    name,
    department,
    salary,
    rank() over(partition by department order by salary desc)as rank_in_dept
from employee1;

select
	employee_id,
    name,
    department,
    salary,
    dense_rank() over(order by salary desc)as rank_in_dept
from employee1;

select
	employee_id,
    name,
    salary,
    ntile(3) over(order by salary desc)as salary_quartile
from employee1;
DELIMITER //
create function calculaterectanglearea(length float,width float)
returns float
deterministic -- it is function always returns the same results if given the
begin
	return length*width;
end //
DELIMITER ;
select calculaterectanglearea(5.5,2.3) as area;

select 
	employee_id,
    salary,
    case
		when salary >100000 then 'high'
        when salary between 50000 and 100000 then 'medium'
        else 'low'
	end as salary_gradw
from employee1;

select * from orders
where
	status=case
				when customer_type='vip' then 'priority'
                else 'standard'
			end;

update products
set price=
	case
		when category='electronics' then price *0.9
        when category='clothing' then price*0.8
        else price
	end;

select name, age,
case
	when age<18 then 'minor'
    when  age between 18 and 59 then 'adult'
    else 'senior'
end as age_group
from people;

update student
set grade=
	case
		when marks>=90 then 'A'
        when marks>=70 then 'B'
        when marks>=80 then 'C'
        else 'D'
	end;

explain select * from employees2 where department_id=5;

insert into users1 values(1,'{"name":"alice","skills":["sql","python"]}');
select JSON_EXTRACT(profile,'$.skills[0]') from users1;

CREATE TABLE employeesNew (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT
);
 
INSERT INTO employeesNew (id, name, manager_id) VALUES
(1, 'Alice (CEO)', NULL),
(2, 'Bob (CTO)', 1),
(3, 'Charlie (CFO)', 1),
(4, 'David (Dev Manager)', 2),
(5, 'Eve (Developer)', 4),
(6, 'Frank (Intern)', 5);

with recursive employee_hierarchy as(
	select id,name,manager_id, 1 as level,
    cast(name as char(1000)) as path
    from employeesNew
    where manager_id is null
);

WITH RECURSIVE
employee_hierarchy AS (
    SELECT 
        id,
        name,
        manager_id,
        1 AS level,
        CAST(name AS CHAR(1000)) AS path
    FROM employeesNew
    WHERE manager_id IS NULL  -- Root (e.g., CEO)
 
    UNION ALL
 
    SELECT 
        e.id,
        e.name,
        e.manager_id,
        eh.level + 1,
        CONCAT(eh.path, ' → ', e.name)
    FROM employeesNew e
    JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
select*from employee_hierarchy;