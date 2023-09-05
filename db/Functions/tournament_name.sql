DELIMITER $$
CREATE FUNCTION tournament_name (tournament_year INT, country VARCHAR(100)) 
RETURNS VARCHAR(200)
DETERMINISTIC
BEGIN 
	DECLARE result_name VARCHAR(200);
    SELECT CONCAT(country, " - ", tournament_year) INTO result_name;
    RETURN result_name;
END $$
DELIMITER ;