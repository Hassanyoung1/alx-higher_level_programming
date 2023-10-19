-- lists all records of the table second_table
-- not listing  rows without a name value

SELECT `score`, `name` FROM `second_table`
WHERE `name` <> ""
ORDER BY `score` DESC;
