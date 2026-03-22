-- Write your PostgreSQL query statement below
SELECT b.name AS Department, a.name as Employee, a.salary
FROM
(
SELECT name, salary, departmentId, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
FROM Employee
) a
JOIN Department b
ON a.departmentId = b.id
WHERE a.rnk <= 3
