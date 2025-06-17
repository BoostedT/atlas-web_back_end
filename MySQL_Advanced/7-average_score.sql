-- This script creates a stored procedure to compute the average score for a given user_id

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE avg_score FLOAT;

  -- Compute the average score for the given user_id
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE user_id = user_id;

  -- Update the average score in the users table
  UPDATE users
  SET average_score = avg_score
  WHERE user_id = user_id;
END$$

DELIMITER ;