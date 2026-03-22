-- Write your PostgreSQL query statement below
WITH adj_ids AS (SELECT 
    id,
    LAG(id, 1) OVER(ORDER BY id) as prev_id,
    LEAD(id, 1) OVER(ORDER BY id) as next_id
FROM Seat
)

(SELECT b.id, a.student
FROM Seat a
JOIN adj_ids b
ON a.id = (CASE WHEN b.id % 2 = 1 THEN b.next_id ELSE b.prev_id END)
ORDER BY b.id
)
UNION ALL 
(
    SELECT id, student
    FROM Seat
    WHERE id = (SELECT MAX(id) FROM Seat HAVING COUNT(*) % 2 = 1)
)
