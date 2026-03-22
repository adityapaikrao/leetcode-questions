-- Write your PostgreSQL query statement below
SELECT CASE 
        WHEN id % 2 = 1 AND (SELECT MAX(id) FROM Seat) = id THEN id
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        END AS id, student
FROM Seat
ORDER BY id