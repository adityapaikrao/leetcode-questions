-- Write your PostgreSQL query statement below
SELECT machine_id, ROUND(AVG(end_time - start_time)::NUMERIC, 3) AS processing_time
FROM
(
    SELECT machine_id, process_id, MAX(timestamp) as end_time, MIN(timestamp) as start_time
    FROM Activity
    GROUP BY machine_id, process_id
)
GROUP BY machine_id