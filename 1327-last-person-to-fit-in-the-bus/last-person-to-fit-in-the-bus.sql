-- Write your PostgreSQL query statement below
WITH cum_weights AS (
    SELECT person_id,
    person_name,
    SUM(weight) OVER (
        ORDER BY turn ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cum_weight
    FROM Queue
)

-- SELECT * 
-- FROM cum_weights

SELECT person_name
FROM cum_weights
WHERE cum_weight <= 1000
ORDER BY cum_weight DESC
LIMIT 1 