-- Write your query below
-- ALL customers w/ positive revenue in 2020
SELECT customer_id
FROM customers
WHERE year = 2020 AND revenue > 0;