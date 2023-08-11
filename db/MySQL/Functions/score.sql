DELIMITER $$
CREATE FUNCTION score (goals_for INT, goals_against INT) 
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN 
	DECLARE result_score VARCHAR(10) DEFAULT "";
    SELECT CONCAT(goals_for, "-", goals_against) INTO result_score;
    RETURN result_score;
END $$
DELIMITER ;