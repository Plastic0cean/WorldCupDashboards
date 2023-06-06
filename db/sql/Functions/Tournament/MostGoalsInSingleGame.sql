CREATE FUNCTION MostGoalsInSingleGame(@tournament_id VARCHAR(100)=NULL)
RETURNS TABLE AS RETURN

WITH MatchResults AS (
SELECT 
	tournament_id,
	match_date,
	home_team_id,
	home_team_name,
	away_team_id,
	away_team_name,
	score,
	home_team_score,
	away_team_score,
	CAST(home_team_score AS INT) + CAST(away_team_score AS INT) AS number_of_goals
FROM matches
WHERE tournament_id = COALESCE(@tournament_id, tournament_id))

SELECT * FROM MatchResults WHERE number_of_goals = (SELECT MAX(number_of_goals) FROM MatchResults)