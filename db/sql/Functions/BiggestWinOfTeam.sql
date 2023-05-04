CREATE FUNCTION BiggestWinOfTeam (@TeamId AS VARCHAR(2000))
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
		CONCAT(goals_for, '-', goals_against) as score
	FROM [team_appearances] 
	WHERE team_id = @TeamId AND Win=1 AND ABS(goal_differential) = (SELECT MAX(ABS(goal_differential)) FROM [team_appearances] WHERE team_id = @TeamId AND Win=1)
GO
