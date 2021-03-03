-- list all cities of california
SELECT id, name
from cities 
WHERE stated_id = ( SELECT id
					FROM states
					WHERE name = "California")
ORDER BY id ASC;
