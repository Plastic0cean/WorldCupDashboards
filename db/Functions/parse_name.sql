DELIMITER $$
CREATE FUNCTION parse_name (given_name Varchar(100), family_name VARCHAR(100)) 
RETURNS Varchar(200)
DETERMINISTIC
BEGIN
    DECLARE result_name VARCHAR(200) DEFAULT "";
    SELECT TRIM(CONCAT(COALESCE(given_name, ""), " ", family_name)) INTO result_name;  
    RETURN result_name;  
END $$  
DELIMITER ;