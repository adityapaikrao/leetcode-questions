-- Write your PostgreSQL query statement below
-- DECLARE low_count INTEGER;
-- DECLARE avg_count INTEGER;
-- DECLARE high_count INTEGER;

WITH category_counts AS (SELECT 
    COUNT(CASE WHEN income < 20000 THEN income END) as low_salary_count,
    COUNT(CASE WHEN income BETWEEN 20000 AND 50000 THEN income END) as avg_salary_count,
    COUNT(CASE WHEN income > 50000 THEN income END) as high_salary_count
FROM Accounts
)

SELECT 'Low Salary'  AS category, low_salary_count AS accounts_count
FROM category_counts

UNION

SELECT 'Average Salary'  AS category, avg_salary_count AS accounts_count
FROM category_counts

UNION

SELECT 'High Salary'  AS category, high_salary_count AS accounts_count
FROM category_counts



