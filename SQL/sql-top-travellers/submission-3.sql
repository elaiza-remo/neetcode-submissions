-- Write your query below
-- Write a query to calculate the total distance traveled by each user.
SELECT users.name, COALESCE(SUM(rides.distance), 0) as travelled_distance
FROM users
LEFT JOIN rides
ON users.id = rides.user_id
GROUP BY users.name
ORDER by COALESCE(SUM(rides.distance),0) DESC, users.name ASC;
