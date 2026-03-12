-- Write your PostgreSQL query statement below
SELECT 
    TO_CHAR(t.trans_date, 'YYYY-MM') AS month,
    t.country,
    COUNT(t.id) AS trans_count,
    COUNT(CASE WHEN t.state = 'approved' THEN 1 ELSE NULL END) AS approved_count,
    SUM(t.amount) AS trans_total_amount,
    SUM(CASE WHEN t.state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions t
GROUP BY month, country
