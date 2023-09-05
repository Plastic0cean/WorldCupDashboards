CREATE PROCEDURE MatchesAsStarterOrSubstitute (playerid VARCHAR(10))
	SELECT 
		COUNT(*) AS total_appearances,
		SUM(starter) AS starter, 
		SUM(substitute) AS substitute 
	FROM player_appearances
	WHERE player_id = playerid;