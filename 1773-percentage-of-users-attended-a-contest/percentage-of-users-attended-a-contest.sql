-- Write your PostgreSQL query statement below
SELECT contest_id, ROUND(COUNT(user_id) / (SELECT COUNT(user_id)::NUMERIC FROM Users), 4) * 100 AS "percentage"
FROM Register 
GROUP BY contest_id
ORDER BY "percentage" DESC, contest_id
