# Write your MySQL query statement below
SELECT T.id AS Id, (CASE WHEN T.p_id IS NULL THEN 'Root'
                   WHEN T.id IN (SELECT DISTINCT T2.p_id AS id
                                 FROM tree T2) THEN 'Inner'
                   ELSE 'Leaf' END) AS Type
FROM tree T
