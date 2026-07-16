-- Write your PostgreSQL query statement below
WITH ranked_employees AS (
SELECT e.departmentId, e.name, e.salary, DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
FROM Employee e 
)

SELECT d.name as department, r.name as employee, salary
FROM Department d
JOIN ranked_employees r 
ON d.id = r.departmentId
WHERE rnk <= 3
