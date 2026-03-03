-- Write your PostgreSQL query statement below
WITH email_counts AS (
    SELECT email, COUNT(id) as email_count
    FROM Person 
    GROUP BY email
)

SELECT email AS Email
FROM email_counts
WHERE email_count >= 2