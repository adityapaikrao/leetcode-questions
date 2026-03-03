-- Write your PostgreSQL query statement below
SELECT cw.id 
FROM Weather AS cw
JOIN Weather AS pw
ON pw.recordDate = (cw.recordDate - INTERVAL '1 days')
WHERE cw.temperature > pw.temperature

