-- Write your PostgreSQL query statement below
SELECT 
    e.employee_id,
    e.name,
    r.reports_count,
    r.average_age
FROM Employees e 
JOIN
    (
        SELECT reports_to as manager_id,
            COUNT(employee_id) as reports_count,
            CAST(AVG(age) AS INTEGER) as average_age
        FROM Employees 
        GROUP BY reports_to
    ) r
ON e.employee_id = r.manager_id
ORDER BY e.employee_id
