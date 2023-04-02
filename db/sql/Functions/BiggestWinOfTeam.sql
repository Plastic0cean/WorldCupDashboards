CREATE FUNCTION BiggestWinOfTeam (@TeamName AS VARCHAR(2000))
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
	WHERE team_name = @TeamName AND Win=1 AND ABS(goal_differential) = (SELECT MAX(ABS(goal_differential)) FROM [team_appearances] WHERE team_name = @TeamName AND Win=1)
GO