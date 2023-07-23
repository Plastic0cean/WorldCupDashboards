DELIMITER //
CREATE PROCEDURE TopScorers (teamid VARCHAR(10))
	BEGIN
	SELECT 
		g.player_id,
		parse_name(p.given_name, p.family_name) AS player_name,
		COUNT(*) AS goals_number
	FROM goals g 
	JOIN players p ON g.player_id = p.player_id
	WHERE team_id = teamid
	GROUP BY g.player_id, p.given_name, p.family_name;
END //
DELIMITER ; 