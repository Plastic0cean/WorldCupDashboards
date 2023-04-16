CREATE FUNCTION BiggestDefeatOfTeam (@TeamId AS VARCHAR(2000))
RETURNS TABLE 
AS 
RETURN 
	SELECT 
		tournament_id, 
		tournament_name, 
		team_name, 
		opponent_id, 
		opponent_name, 
		match_name, 
		match_date, 
		CONCAT(goals_for, '-', goals_against) as Score
	FROM [team_appearances] 
	WHERE team_id = @TeamId AND Lose=1 AND ABS(goal_differential) = (SELECT MAX(ABS(CAST(goal_differential as Int))) FROM [team_appearances] WHERE team_id = @TeamId AND Lose=1)
GO

