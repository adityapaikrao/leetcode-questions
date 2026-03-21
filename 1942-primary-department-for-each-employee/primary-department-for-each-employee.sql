-- Write your PostgreSQL query statement below
SELECT a.employee_id,
    a.department_id
FROM Employee a
JOIN 
(
    SELECT employee_id,
        COUNT(department_id) as num_departments
    FROM Employee 
    GROUP BY employee_id
) b
ON a.employee_id = b.employee_id
AND (b.num_departments = 1 OR (b.num_departments > 1 AND a.primary_flag = 'Y'))