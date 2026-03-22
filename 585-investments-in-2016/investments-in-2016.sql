-- Write your PostgreSQL query statement below
WITH tiv_2015_counts AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(pid) > 1
),
lat_lon_counts AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(pid) = 1
)

SELECT ROUND(sum(tiv_2016)::NUMERIC, 2) AS tiv_2016
FROM Insurance 
WHERE tiv_2015 IN (SELECT tiv_2015 FROM tiv_2015_counts)
AND (lat, lon) IN (SELECT lat, lon FROM lat_lon_counts)
