-- Write your PostgreSQL query statement below
WITH student_subjects AS (
    SELECT *
    FROM Students st
    CROSS JOIN Subjects sb
)


SELECT 
    ss.student_id, 
    ss.student_name, 
    ss.subject_name, 
    COUNT(ex.subject_name)  AS attended_exams
FROM student_subjects ss
LEFT JOIN Examinations ex
ON ss.student_id = ex.student_id
AND ss.subject_name = ex.subject_name
GROUP BY ss.student_id, ss.student_name, ss.subject_name

-- SELECT 
--     ss.student_id, 
--     ss.student_name AS student_name_ss, 
--     ss.subject_name AS subject_name_ss,
--     ex.* 
--     -- COUNT(CASE WHEN ex.subject_name is NULL THEN 0 ELSE 1 END)
-- FROM student_subjects ss
-- LEFT JOIN Examinations ex
-- ON ss.student_id = ex.student_id
-- AND ss.subject_name = ex.subject_name

