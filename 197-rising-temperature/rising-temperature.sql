-- Write your PostgreSQL query statement below
SELECT cw.id 
FROM Weather AS cw
LEFT JOIN Weather AS pw
ON pw.recordDate = (cw.recordDate - INTERVAL '1 days')
WHERE cw.temperature > pw.temperature

