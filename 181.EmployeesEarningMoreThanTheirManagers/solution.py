# Write your MySQL query statement below
SELECT E.Name AS Employee
FROM Employee E
WHERE E.Salary > (SELECT Salary
                 FROM Employee E2
                 WHERE E2.Id = E.ManagerId)
