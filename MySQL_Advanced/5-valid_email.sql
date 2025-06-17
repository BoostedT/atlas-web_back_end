-- This script creates a table with a trigger to validate email addresses.

DELIMITER $$

CREATE TRIGGER before_user_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END$$

DELIMITER ;