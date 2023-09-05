CREATE PROCEDURE GoalsByTournament (teamid VARCHAR(10))
SELECT 
	tournament_name(t.year, t.host_country) AS tournament_name,
	SUM(goals_for) AS number_of_goals
FROM team_appearances a JOIN tournaments t ON t.tournament_id = a.tournament_id
WHERE team_id = teamid
GROUP BY t.year, t.host_country
HAVING SUM(goals_for)>0;