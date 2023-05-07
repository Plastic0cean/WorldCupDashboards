CREATE FUNCTION PlayersList()
RETURNS TABLE AS 
RETURN 
		WITH ListOfPlayersTemp AS (
	SELECT 
		ROW_NUMBER() OVER(PARTITION BY p.player_id ORDER BY p.player_id) AS RowNumber,
		p.player_id AS PlayerId,
		COALESCE(p.given_name, '') AS given_name,
		COALESCE(p.family_name, '') AS family_name,
		LTRIM(CONCAT(p.given_name, ' ', p.family_name)) as Name,
		s.position_name AS position,
		s.team_id AS team_id,
		s.team_name AS nationality
	FROM players p 
	LEFT JOIN squads s ON p.player_id = s.player_id
	WHERE p.player_id IN (SELECT player_id FROM player_appearances))
		  
	SELECT 
		PlayerId,
		given_name,
		family_name,
		[Name],
		[position],
		[team_id],
		[nationality]
	FROM ListOfPlayersTemp WHERE RowNumber = 1;

GO