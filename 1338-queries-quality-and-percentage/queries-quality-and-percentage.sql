-- Write your PostgreSQL query statement below
SELECT 
    q.query_name,
    ROUND(AVG(rating::NUMERIC / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)::NUMERIC / COUNT(*), 4) * 100 AS poor_query_percentage
FROM Queries q
GROUP BY q.query_name


