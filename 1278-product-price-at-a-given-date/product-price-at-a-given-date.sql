-- Write your PostgreSQL query statement below
WITH products_at_10 AS (
    SELECT product_id
    FROM Products 
    GROUP BY product_id
    HAVING MIN(change_date) > '2019-08-16'
)

SELECT a.product_id, a.new_price AS price
FROM Products a
RIGHT JOIN
(SELECT product_id, MAX(change_date) AS max_date
FROM Products
WHERE change_date <= '2019-08-16'
GROUP BY product_id
) b 
ON a.product_id = b.product_id
AND a.change_date = b.max_date
UNION
( SELECT product_id, 10 AS price FROM products_at_10)

-- SELECT product_id, MAX(change_date) AS max_date
-- FROM Products
-- WHERE change_date <= '2019-08-16'
-- GROUP BY product_id

-- SELECT product_id
--     FROM Products 
--     GROUP BY product_id
--     HAVING MIN(change_date) > '2019-08-16'