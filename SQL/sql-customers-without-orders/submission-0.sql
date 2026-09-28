-- Write your query below
-- Return customer names who have NEVER placed an order 
SELECT customers.name
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id
WHERE orders.id is NULL