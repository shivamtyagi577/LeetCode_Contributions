# Write your MySQL query statement below
#select salary from Employee where salary not in (select max(salary) from employee) order by salary desc top 1;

select max(salary) as SecondHighestSalary from employee where salary < (select max(salary) from employee)