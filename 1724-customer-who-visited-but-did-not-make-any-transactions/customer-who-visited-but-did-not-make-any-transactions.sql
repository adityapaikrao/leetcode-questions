-- Write your PostgreSQL query statement below
WITH customer_visit_transactions AS (
    SELECT v.customer_id, v.visit_id, count(t.transaction_id) AS count_transactions
    FROM Visits AS v
    LEFT JOIN Transactions AS t
    ON v.visit_id = t.visit_id
    GROUP BY v.customer_id, v.visit_id
)

SELECT customer_id, count(visit_id) AS count_no_trans
FROM customer_visit_transactions
WHERE count_transactions = 0
GROUP BY customer_id
