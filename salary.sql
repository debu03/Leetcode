# Write your MySQL query statement below
#Write a solution to find the employees who earn more than their managers.


select name as Employee 
from Employee e 
where salary>(select salary from Employee where id=e.managerId);