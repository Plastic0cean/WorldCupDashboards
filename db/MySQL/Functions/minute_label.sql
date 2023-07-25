DELIMITER $$
CREATE FUNCTION minute_label (minute_regulation INT, minute_stoppage INT) 
RETURNS Varchar(50)
DETERMINISTIC
BEGIN
    DECLARE result_minute VARCHAR(50) DEFAULT "";
    
    SELECT 
		IF(minute_stoppage IS NULL, CONCAT(minute_regulation, "'"), CONCAT(minute_regulation, "+", minute_stoppage, "'"))
	INTO result_minute;  
    
    RETURN result_minute;  
END $$  
DELIMITER ;