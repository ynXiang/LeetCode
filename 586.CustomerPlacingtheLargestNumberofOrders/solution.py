# Write your MySQL query statement below
SELECT O.customer_number
FROM orders O
GROUP BY O.customer_number
ORDER BY COUNT(*) DESC LIMIT 1
