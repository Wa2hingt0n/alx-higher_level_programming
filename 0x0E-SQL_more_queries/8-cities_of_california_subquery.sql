-- Lists all the cities of California` in ascending orderof cities.id
SELECT `id`, `name` FROM cities WHERE `state_id` = (SELECT `id` FROM states
WHERE `name` = "California") ORDER BY `id` ASC;
