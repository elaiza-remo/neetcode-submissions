-- Write your query below
-- Return the employee_id and bonus for each employee, ordered by employee_id. 
-- calculate the bonus for each employee. An employee receives a bonus equal to 100% of their salary if: Their employee_id is an odd number, AND Their name does not start with the letter 'M'

SELECT employee_id,
CASE
    WHEN (MOD(employee_id, 2) = 1) AND name NOT LIKE 'M%' THEN salary
    ELSE 0 
END AS bonus
FROM employees
ORDER BY employee_id ASC;