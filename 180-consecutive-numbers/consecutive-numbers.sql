-- Write your PostgreSQL query statement below
WITH num_logs AS (
    SELECT num,
    LAG(num, 1) OVER (ORDER BY id) as prev1,
    LAG(num, 2) OVER (ORDER BY id) as prev2
    FROM Logs
)

SELECT DISTINCT num as ConsecutiveNums
FROM num_logs
WHERE num = prev1 and prev1 = prev2
