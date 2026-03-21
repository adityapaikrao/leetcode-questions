-- Write your PostgreSQL query statement below
WITH num_lags AS (
SELECT num,
    LAG(num, 1) OVER (ORDER BY id) AS prev1,
    LAG(num, 2) OVER (ORDER BY id) AS prev2
FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROm num_lags
WHERE num = prev1 AND prev1 = prev2