CREATE PROCEDURE PlayerMinutesPlayedByMatches (playerid VARCHAR(10))
SELECT 
	minutes_played,
	CASE 
		WHEN extra_time = 0 THEN 90
		ELSE 120
	END AS possible_minutes
FROM matches m
JOIN player_appearances a ON m.match_id = a.match_id
WHERE playerid = playerid;