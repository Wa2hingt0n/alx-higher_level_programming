-- Lists all records with a score >= 10 in the table 'second_table'
-- with the records showing score and name and ordered by score
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10
ORDER BY `score` DESC;
