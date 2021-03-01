-- list the number of record
SELECT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;
