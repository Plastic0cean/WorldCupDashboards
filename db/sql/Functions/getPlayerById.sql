CREATE FUNCTION GetPlayerById (@player_id VARCHAR(10))
RETURNS TABLE AS 
RETURN 
	SELECT TOP 1 
		CONCAT(p.given_name, ' ', p.family_name) as [name],
		birth_date,
		team_name as team, 
		position_name as position 
	FROM Players p 
	LEFT JOIN [squads] s ON s.player_id = p.player_id
	WHERE p.player_id = @player_id
