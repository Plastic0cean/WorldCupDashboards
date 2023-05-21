CREATE FUNCTION AllMatchesByTeam(@team_id VARCHAR(20))
RETURNS TABLE 
AS RETURN 
	SELECT 
		lose, 
		draw, 
		CAST(match_date AS date) as match_date, 
		match_id, 
		win, 
		opponent_name, 
		opponent_code, 
		CONCAT(goals_for, ' - ', goals_against) as score, 
		CAST(goal_differential AS INT) AS goal_differential
    FROM team_appearances WHERE team_id=@team_id