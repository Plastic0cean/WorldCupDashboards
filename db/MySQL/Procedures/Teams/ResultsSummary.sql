DELIMITER //
CREATE PROCEDURE ResultsSummary (teamid VARCHAR(10))
BEGIN
	SELECT 
		SUM(win) AS wins,
		SUM(lose) AS loses,
		SUM(draw) AS draws
	FROM team_appearances 
	WHERE team_id = teamId;
END //
DELIMITER ; 