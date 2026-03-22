-- Write your PostgreSQL query statement below
WITH daily_amounts AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT visited_on, amount, ROUND(average_amount, 2) AS average_amount
FROM 
(
SELECT MAX(visited_on) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS visited_on,
      SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
      AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
FROM daily_amounts
)
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + 6