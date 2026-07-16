-- Write your PostgreSQL query statement below
WITH highest_user AS (
    SELECT m.user_id, u.name, COUNT(m.movie_id) as review_counts
    FROM MovieRating m 
    JOIN Users u 
    ON m.user_id = u.user_id
    GROUP BY m.user_id, u.name
    ORDER BY review_counts DESC, u.name ASC
    LIMIT 1
),
highest_avg_movie AS (
    SELECT mr.movie_id, m.title, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m
    ON mr.movie_id = m.movie_id
    WHERE TO_CHAR(mr.created_at, 'YYYY-MM') = '2020-02'
    GROUP BY mr.movie_id, m.title
    ORDER BY avg_rating DESC, m.title ASC
    LIMIT 1

)


(SELECT h.name AS "results" FROM highest_user h)
UNION ALL 
(SELECT h.title AS "results" FROM highest_avg_movie h)