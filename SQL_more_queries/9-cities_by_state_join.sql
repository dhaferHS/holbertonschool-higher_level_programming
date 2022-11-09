--  lists all cities contained in the database hbtn_0d_usa.
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name FROM cities C INNER JOIN states S ON C.states.id = S.id ORDER BY C.id;