-- Write your PostgreSQL query statement below
WITH user_confirmations AS (
    SELECT 
        sg.user_id, 
        SUM(CASE WHEN cnf.action = 'confirmed' THEN 1 ELSE 0 END) AS user_confirmations,
        SUM(CASE WHEN cnf.action = 'timeout' THEN 1 ELSE 0 END) AS user_timeouts
        FROM Signups sg
        LEFT JOIN Confirmations cnf
        ON sg.user_id = cnf.user_id
        GROUP BY sg.user_id
)

SELECT 
    user_id, 
    ROUND((CASE WHEN user_timeouts = 0 AND user_confirmations = 0 THEN 0 ELSE user_confirmations::NUMERIC/(user_timeouts + user_confirmations)::NUMERIC END), 2) AS confirmation_rate

    FROM user_confirmations
    