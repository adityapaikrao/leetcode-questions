-- Write your PostgreSQL query statement below
WITH emp_manager_salary AS (
SELECT emp1.name, emp1.salary, emp2.salary AS managerSalary
FROM Employee emp1
JOIN Employee emp2 
ON emp1.managerId = emp2.id
)

SELECT t.name AS Employee
FROM emp_manager_salary t
WHERE salary > managerSalary