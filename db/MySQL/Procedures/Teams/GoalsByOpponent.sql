CREATE PROCEDURE GoalsByOpponent (teamid VARCHAR(10))
SELECT 
	t.team_name AS opponent_name,
	SUM(goals_for) AS number_of_goals
FROM team_appearances a 
JOIN teams t ON t.team_id = a.opponent_id
WHERE a.team_id = teamid
GROUP BY opponent_name
HAVING SUM(goals_for) > 0;
