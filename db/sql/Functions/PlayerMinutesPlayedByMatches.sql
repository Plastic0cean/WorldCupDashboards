CREATE FUNCTION PlayerMinutesPlayedByMatches (@player_id VARCHAR(20))
RETURNS TABLE
AS RETURN 
	
WITH player_matches AS (
	SELECT 
		m.match_name,
		m.match_id,
		p.tournament_name,
		minute_regulation,
		going_off, 
		coming_on,
		starter, 
		substitute,
		CASE 
			WHEN extra_time = 0 THEN 90
			ELSE 120
		END AS possible_minutes
	FROM player_appearances p 
	JOIN matches m ON m.match_id = p.match_id
	LEFT JOIN substitutions s ON p.player_id = s.player_id AND m.match_Id = s.match_id
	WHERE p.player_id = @player_id	
	)

	SELECT 
		*, 
		CASE 
			WHEN starter = '1' THEN COALESCE(minute_regulation, possible_minutes)
			WHEN starter = '0' THEN possible_minutes - CAST(minute_regulation AS INT)
		END AS minutes_played
	FROM player_matches


