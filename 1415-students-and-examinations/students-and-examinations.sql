-- Write your PostgreSQL query statement below
SELECT st.student_id, st.student_name, su.subject_name, COUNT(ex.student_id) AS attended_exams
FROM Students st 
CROSS JOIN Subjects su
LEFT JOIN Examinations ex
ON su.subject_name = ex.subject_name
AND st.student_id = ex.student_id
GROUP BY 1, 2, 3