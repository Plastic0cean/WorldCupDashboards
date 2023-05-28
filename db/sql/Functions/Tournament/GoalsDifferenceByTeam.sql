 CREATE FUNCTION GoalsDifferenceByTeam(@tournament_id VARCHAR(10))
 RETURNS TABLE 
 AS RETURN 
	SELECT
		team_name,
		SUM(CAST(goals_for AS INT)) AS goals_for,
		SUM(CAST(goals_against AS INT)) AS goals_against,
		SUM(CAST(goals_for AS INT) - CAST(goals_against AS INT)) AS goals_difference
	FROM team_appearances 
	WHERE tournament_id = COALESCE(@tournament_id, tournament_id)
	GROUP BY team_name 
GO 