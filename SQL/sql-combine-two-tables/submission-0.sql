-- Write your query below
SELECT person.first_name, person.last_name, address.city, address.state
FROM person
FULL OUTER JOIN address
ON address.person_id = person.person_id
WHERE person.first_name IS NOT NULL;