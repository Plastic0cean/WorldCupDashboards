CREATE FUNCTION PlayersList()
RETURNS TABLE AS 
RETURN 
		--This code is too slow 
		--Before I figure out how to make it faster, I will use simpler approach
	--SELECT DISTINCT 
	--	p.player_id AS PlayerId,
	--	CONCAT(p.given_name, ' ', p.family_name) AS [Name],
	--	s.position_name AS Position,
	--	s.team_id AS TeamId,
	--	s.team_name AS Nationality
	--FROM players p 
	--LEFT JOIN squads s ON p.player_id = s.player_id;

	SELECT 
		player_id AS PlayerId,
		CONCAT(given_name, ' ', family_name) AS [Name]
	FROM players


GO