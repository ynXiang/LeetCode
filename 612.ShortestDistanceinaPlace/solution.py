# Write your MySQL query statement below
SELECT CAST(SQRT(MIN((P1.x-P2.x)*(P1.x-P2.x)+(P1.y-P2.y)*(P1.y-P2.y))) AS DECIMAL(5,2)) AS shortest
FROM point_2d P1, point_2d P2
WHERE P1.x != P2.x OR P1.y != P2.y
