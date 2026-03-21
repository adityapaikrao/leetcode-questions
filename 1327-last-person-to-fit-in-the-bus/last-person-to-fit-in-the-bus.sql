-- Write your PostgreSQL query statement below
SELECT person_name
FROM
(SELECT person_id, person_name,
    SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_wt
FROM Queue 
-- GROUP BY q.person_id, person_name
)
WHERE running_wt <= 1000 
ORDER BY running_wt DESC
LIMIT 1

-- SELECT person_id, person_name,
--     SUM(weight) OVER (ORDER BY turn) AS running_wt
-- FROM Queue 