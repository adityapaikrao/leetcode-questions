-- Write your PostgreSQL query statement below
SELECT 
    TO_CHAR(t.trans_date, 'YYYY-MM') AS month,
    t.country,
    COUNT(t.id) AS trans_count,
    COUNT(t.id) FILTER (WHERE t.state = 'approved') AS approved_count,
    SUM(t.amount) AS trans_total_amount,
    COALESCE(SUM(amount) FILTER (WHERE t.state = 'approved'), 0) AS approved_total_amount
FROM Transactions t
GROUP BY month, country
