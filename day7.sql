use DataRevature;
create table products(productId int, productname varchar(20),price int);
insert into products values(1,'bike',100000),(2,'car',500000),(3,'b1',1000),(4,'c1',9000000);
select * from products;
select min(price) 
from products;
select min(price) as smallestprice, productId
from products
group by productId;
select count(productId)
from products
where price>20000;
insert into products values(5,'a',100000);
select count(distinct price) from products;
select sum(price) from products;
select avg(price) from products;
-- cascade
create table customers(
	customer_id int primary key,
    name varchar(100)
);
create table orders(
	order_id int primary key,
    customer_id int,
    product varchar(100),
    foreign key (customer_id)references customers(customer_id)
    on delete cascade
);
insert into customers values(1,'sreeja'),(2,'shreya');
insert into orders values(101,1,'laptop'),(102,1,'phone'),(103,2,'tablet');
select * from customers;
select * from orders;
delete from customers where customer_id=1;
select * from customers;
select * from orders;
create table employee(
	department int,
    salary int,
    name varchar(100)
);
insert into employee values(1,3000,'sreeja'),(12,1300,'navya'),(3,4000,'shreya');
select*from employee order by salary;
select*from employee order by salary desc;
select* from employee order by department asc, salary desc;
select name, salary * 12 as annual_salary
from employee
order by annual_salary desc; 
drop table employee;

-- join
CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
); 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);
select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
inner join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;
select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
left join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;
select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
right join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;
select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;
create table drinks(id int, Name varchar(100));
create table snacks(id int,name varchar(100));
insert into drinks values(1,'tea'),(2,'coffee');
insert into snacks values(1,'cake'),(2,'lays');
select drinks.id,drinks.name,snacks.id,snacks.name 
from drinks
cross join snacks;

create table Emp(emp_id int,ename varchar(20),job_desc varchar(25),
salary int,hire_date date);
insert into Emp values(1,'ram','admine',100000,date '2024-02-12'),(2,'george','manager',200000,date '2024-02-12'),(3,'aravind','admine',300000,date '2024-02-1'),(4,'nivetha','sales',250000,date '2024-02-02');
select * from Emp;
select * from Emp order by job_desc;
select job_desc, avg(salary) from Emp group by job_desc;
select job_desc, count(emp_id) from Emp group by job_desc;
select job_desc,count(emp_id)
from Emp
group by job_desc
having count(emp_id)>1
order by job_desc;

select job_desc,count(emp_id)
from Emp where salary>10000
group by job_desc
having count(emp_id)>1
order by job_desc;

