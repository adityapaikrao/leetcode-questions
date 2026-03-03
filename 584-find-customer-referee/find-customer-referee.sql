-- Write your PostgreSQL query statement below
SELECT c.name
FROM Customer c
WHERE c.referee_id is null OR c.referee_id != 2