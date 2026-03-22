-- Write your PostgreSQL query statement below
WITH most_requests AS (
    SELECT requester_id, COUNT(*) AS count_friends
    FROM RequestAccepted
    GROUP BY requester_id
),
most_accepts AS (
    SELECT accepter_id, COUNT(*) AS count_friends
    FROM RequestAccepted
    GROUP BY accepter_id
)

SELECT a.id, SUM(a.num) AS num
FROM
(
SELECT requester_id AS id, count_friends AS num
FROM most_requests
UNION ALL
SELECT accepter_id AS id, count_friends AS num 
FROM most_accepts
) a
GROUP BY a.id
ORDER BY num DESC
LIMIT 1
