CREATE FUNCTION PlayerNumberOfMatches (@player_id VARCHAR(10))
RETURNS TABLE 
AS RETURN
SELECT 
	COUNT(*) AS total_appearances,
	SUM(CAST(starter as INT)) AS starter, 
	SUM(CAST(substitute AS INT)) AS substitute 
FROM player_appearances
WHERE player_id= @player_id
