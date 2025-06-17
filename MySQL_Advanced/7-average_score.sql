-- This script creates a stored procedure to compute the average score for a given user_id

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN uid INT)
BEGIN
  DECLARE avg_score FLOAT;

  -- Compute the average score for the given user_id
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE user_id = uid;

  -- Update the average score in the users table
  UPDATE users
  SET average_score = IFNULL(avg_score, 0)
  WHERE id = uid;
END$$

DELIMITER ;