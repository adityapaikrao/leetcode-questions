-- Write your PostgreSQL query statement below
SELECT *
FROM Cinema cn
WHERE cn.id % 2 = 1
AND cn.description != 'boring'
ORDER BY cn.rating DESC