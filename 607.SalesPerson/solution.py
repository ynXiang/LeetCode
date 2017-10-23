# Write your MySQL query statement below
SELECT S.name
FROM salesperson S
WHERE NOT EXISTS (SELECT *
                  FROM orders O
                  RIGHT JOIN company C
                  ON C.com_id = O.com_id AND C.name = 'RED'
                  WHERE S.sales_id = O.sales_id)
