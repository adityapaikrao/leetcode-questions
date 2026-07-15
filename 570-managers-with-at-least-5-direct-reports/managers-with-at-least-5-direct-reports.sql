-- Write your PostgreSQL query statement below
SELECT e2.name
FROM
(
    SELECT e1.managerId
    FROM Employee e1
    GROUP BY e1.managerId
    HAVING count(e1.id) >= 5
) a 
JOIN Employee e2
ON a.managerId = e2.id
