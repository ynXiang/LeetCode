# Write your MySQL query statement below
SELECT Max(Salary) AS SecondHighestSalary
FROM Employee E
WHERE E.Salary < (SELECT Max(Salary)
                 FROM Employee)
