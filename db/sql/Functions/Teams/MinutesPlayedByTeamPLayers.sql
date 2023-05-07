CREATE FUNCTION MinutesPlayedByTeamPLayers (@team_id NVARCHAR(10))
RETURNS TABLE 
AS RETURN

WITH minutes_by_players AS (
SELECT 
	p.player_id,
	starter,
	substitute,
	minute_regulation,
	going_off, 
	coming_on,
	LTRIM(CONCAT(p.given_name, ' ', p.family_name)) AS player_name,
	CASE 
		WHEN extra_time = 0 THEN 90
		ELSE 120
	END AS possible_minutes
FROM player_appearances p 
JOIN matches m ON m.match_id = p.match_id
LEFT JOIN substitutions s ON p.player_id = s.player_id AND m.match_Id = s.match_id
WHERE p.team_id = @team_id),

minutes_played_by_players AS (
	SELECT
		player_id,
		player_name, 
		CASE 
			WHEN starter = '1' THEN COALESCE(minute_regulation, possible_minutes)
			WHEN starter = '0' THEN possible_minutes - CAST(minute_regulation AS INT)
		END AS minutes_played
FROM minutes_by_players)

SELECT player_id, player_name, SUM(minutes_played) AS minutes_played FROM minutes_played_by_players
GROUP BY player_id, player_name



