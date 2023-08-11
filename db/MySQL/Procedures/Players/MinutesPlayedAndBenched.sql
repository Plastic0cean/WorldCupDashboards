CREATE PROCEDURE MinutesPlayedAndBenched (playerid VARCHAR(10))
WITH MinutesPlayedByMatches AS (
	SELECT 
		minutes_played,
		CASE 
			WHEN extra_time = 0 THEN 90
			ELSE 120
		END AS possible_minutes
	FROM matches m
	JOIN player_appearances a ON m.match_id = a.match_id
	WHERE player_id = playerid)
	
	SELECT 
		SUM(minutes_played) AS minutes_played,
		SUM(possible_minutes - minutes_played) AS minutes_on_bench
	FROM MinutesPlayedByMatches;
    
