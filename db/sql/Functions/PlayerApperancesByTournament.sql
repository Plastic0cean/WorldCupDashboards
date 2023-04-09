CREATE FUNCTION PlayerApperancesByTournament (@player_id VARCHAR(10))
RETURNS TABLE
AS RETURN 
	SELECT 
		CONCAT(t.[year], ' ', t.host_country) AS tournament, 
		stage_name as stage,
		COUNT(*) AS number_of_matches
	FROM player_appearances p 
	JOIN tournaments t ON p.tournament_id = t.tournament_id
	WHERE player_id = @player_id
	GROUP BY t.[year], t.host_country, stage_name 