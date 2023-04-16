CREATE FUNCTION PlayersList()
RETURNS TABLE AS 
RETURN 
	SELECT DISTINCT 
		p.player_id AS PlayerId,
		COALESCE(p.given_name, '') AS given_name,
		COALESCE(p.family_name, '') AS family_name,
		LTRIM(CONCAT(p.given_name, ' ', p.family_name)) as Name,
		s.position_name AS position,
		s.team_id AS team_id,
		s.team_name AS nationality
	FROM players p 
	LEFT JOIN squads s ON p.player_id = s.player_id;

GO