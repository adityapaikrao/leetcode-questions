-- Write your PostgreSQL query statement below
SELECT 
    p.product_id, 
    CASE 
        WHEN COUNT(u.product_id) = 0 THEN 0
        ELSE ROUND(SUM(p.price * u.units)::NUMERIC/SUM(u.units), 2) 
    END AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id