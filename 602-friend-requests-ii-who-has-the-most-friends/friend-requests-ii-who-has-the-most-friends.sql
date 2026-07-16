-- Write your PostgreSQL query statement below
WITH friend_counts AS (
    SELECT requester_id AS id, COUNT(*) AS counts
    FROM RequestAccepted
    GROUP BY requester_id

    UNION ALL

    SELECT accepter_id AS id, COUNT(*) AS counts
    FROM RequestAccepted
    GROUP BY accepter_id
)

SELECT id, SUM(counts) as num
FROM friend_counts
GROUP BY id
ORDER BY num DESC
LIMIT 1