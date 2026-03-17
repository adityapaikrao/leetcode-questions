-- Write your PostgreSQL query statement below
WITH next_login_dates AS (
    SELECT player_id,
    event_date,
    LEAD(event_date, 1) OVER (PARTITION BY player_id ORDER BY event_date) AS next_date,
    RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity
)

SELECT ROUND(COUNT(player_id)::numeric / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM next_login_dates
WHERE next_date - event_date = 1
AND rnk = 1
