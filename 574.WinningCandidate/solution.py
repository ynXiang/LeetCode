# Write your MySQL query statement below
SELECT C.Name
FROM Candidate C
WHERE C.id = (SELECT CandidateId
             FROM Vote
             GROUP BY CandidateId
             ORDER BY COUNT(*) DESC
             LIMIT 1)
