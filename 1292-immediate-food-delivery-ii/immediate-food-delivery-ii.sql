-- Write your PostgreSQL query statement below
WITH customer_first_orders AS (
    SELECT 
        order_date, customer_pref_delivery_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date ASC
            ) AS row_number
    FROM Delivery
)

SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1.0 ELSE 0.0 END), 4) * 100 AS immediate_percentage
FROM customer_first_orders
WHERE row_number = 1