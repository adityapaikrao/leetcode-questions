-- Write your PostgreSQL query statement below
WITH total_users AS (
    SELECT COUNT(user_id) AS count_users FROM Users
)

SELECT contest_id, ROUND(COUNT(user_id)::NUMERIC * 100 / count_users, 2) AS percentage
FROM Register r
CROSS JOIN total_users
GROUP BY contest_id, count_users
ORDER BY percentage DESC, contest_id ASC