-- Write your PostgreSQL query statement below
SELECT DISTINCT a.employee_id,
    a.department_id
FROM Employee a
WHERE a.primary_flag = 'Y'
OR a.employee_id IN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(*) = 1
)