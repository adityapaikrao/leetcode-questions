-- Write your PostgreSQL query statement below
SELECT email AS Email
FROM Person
GROUP BY email
having count(email) >= 2