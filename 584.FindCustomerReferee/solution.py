# Write your MySQL query statement below
SELECT C.name
FROM customer C
WHERE C.referee_id != 2 OR C.referee_id IS NULL
