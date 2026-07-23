-- Write your PostgreSQL query statement below
SELECT user_id, COUNT(*) as followers_count
FROM Followers
GROUP BY 1
ORDER BY 1