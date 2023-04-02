CREATE FUNCTION PlayerGoalsByTeam (@playerId VARCHAR(20))
RETURNS TABLE AS 
RETURN

SELECT SUM(number_of_goals) AS number_of_goals, team 
FROM (

	SELECT 
	COUNT(*) AS number_of_goals, 
	home_team_name AS [team]
	FROM Goals g 
	JOIN matches m ON m.match_id = g.match_id AND g.team_id <> m.home_team_id 
	WHERE g.Player_Id = @playerId
	GROUP BY g.match_name, m.match_id, home_team_name

	UNION 

	SELECT 
	COUNT(*) AS number_of_goals, 
	m.away_team_name AS team
	FROM Goals g 
	JOIN matches m ON m.match_id = g.match_id AND g.team_id <> m.away_team_id 
	WHERE g.Player_Id = @playerId
	GROUP BY g.match_name, m.match_id, m.away_team_name) as subquery 
GROUP BY team
