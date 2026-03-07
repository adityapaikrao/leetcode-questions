-- Write your PostgreSQL query statement below
-- WITH user_confirmations AS (
SELECT 
    sg.user_id, 
    ROUND(AVG(CASE WHEN cnf.action = 'confirmed' THEN 1 ELSE 0 END), 2) AS confirmation_rate
    FROM Signups sg
    LEFT JOIN Confirmations cnf
    ON sg.user_id = cnf.user_id
    GROUP BY sg.user_id
-- )

-- SELECT 
--     user_id, 
--     ROUND((CASE WHEN user_timeouts = 0 AND user_confirmations = 0 THEN 0 ELSE user_confirmations/(user_timeouts + user_confirmations) END), 2) AS confirmation_rate

--     FROM user_confirmations
    