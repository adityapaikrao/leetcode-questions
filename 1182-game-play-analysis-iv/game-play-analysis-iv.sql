-- Write your PostgreSQL query statement below
SELECT ROUND(COUNT(a.player_id) / COUNT(b.player_id)::NUMERIC, 2) AS fraction
FROM Activity a
RIGHT JOIN 
    (SELECT player_id, MIN(event_date) AS first_date FROM Activity GROUP BY player_id) b
ON a.player_id = b.player_id
AND a.event_date = b.first_date + INTERVAL '1 days'
