# Write your MySQL query statement below
SELECT D.dept_name, IFNULL(Temp.num, 0) AS student_number
FROM department D
LEFT JOIN (SELECT S.dept_id, COUNT(*) as num
          FROM student S
          GROUP BY S.dept_id) AS Temp
ON D.dept_id = Temp.dept_id
ORDER BY Temp.num DESC, D.dept_name
