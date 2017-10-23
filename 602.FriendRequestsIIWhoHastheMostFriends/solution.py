# Write your MySQL query statement below
SELECT Temp.requester_id as id, COUNT(*) as num
FROM (SELECT *
FROM request_accepted R
UNION
SELECT R1.accepter_id, R1.requester_id, R1.accept_date
FROM request_accepted R1) Temp
GROUP BY Temp.requester_id
ORDER BY COUNT(*) DESC LIMIT 1
