-- Create a view named `need_meeting` that selects the names of students

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (
    last_meeting IS NULL
    OR last_meeting < CURDATE() - INTERVAL 1 MONTH
  );