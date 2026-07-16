-- Write your PostgreSQL query statement below
SELECT ROUND(AVG((order_date = customer_pref_delivery_date)::INT), 4) * 100 AS immediate_percentage
FROM Delivery a
JOIN (SELECT customer_id, MIN(order_date) as min_order_date FROM Delivery GROUP BY 1) b 
ON a.customer_id = b.customer_id
AND a.order_date = b.min_order_date