# Write your MySQL query statement below
SELECT IF(F.Cnt = 0, 0.00, CAST(R.Cnt/F.Cnt AS DECIMAL(4,2))) AS accept_rate
FROM (SELECT COUNT(DISTINCT sender_id, send_to_id) AS Cnt
      FROM friend_request) F,
     (SELECT COUNT(DISTINCT requester_id, accepter_id) AS Cnt
      FROM request_accepted) R
