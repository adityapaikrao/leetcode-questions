-- Write your PostgreSQL query statement below
WITH products_10 AS (
    SELECT product_id
    FROM Products 
    GROUP BY product_id
    HAVING MIN(change_date) > '2019-08-16'
), products_changed AS (
    SELECT product_id, change_date
    FROM Products 
    WHERE change_date <= '2019-08-16'
)

SELECT product_id, 10 AS price 
FROM products_10

UNION

SELECT a.product_id, a.new_price AS price
FROM Products a
JOIN (
    SELECT product_id, MAX(change_date) AS change_date_max
    FROM products_changed
    GROUP BY product_id
) b
ON a.product_id = b.product_id
AND a.change_date = b.change_date_max