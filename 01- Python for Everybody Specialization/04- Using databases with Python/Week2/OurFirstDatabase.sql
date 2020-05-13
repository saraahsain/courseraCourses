CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Archibald', 36);
INSERT INTO Ages (name, age) VALUES ('Shazina', 20);
INSERT INTO Ages (name, age) VALUES ('Elli', 19);
INSERT INTO Ages (name, age) VALUES ('Fionnah', 28);
INSERT INTO Ages (name, age) VALUES ('Sno', 13);
INSERT INTO Ages (name, age) VALUES ('Boshra', 23);
SELECT hex(name || age) AS X FROM Ages ORDER BY X
-- 417263686962616C643336