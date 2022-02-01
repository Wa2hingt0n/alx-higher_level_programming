-- Lists all records in the `second_table` table having a name value
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score`
DESC;
