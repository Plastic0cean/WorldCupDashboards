CREATE PROCEDURE GoalsDifferenceByTeam (tournament_id VARCHAR(10))
SELECT 
	t.team_name,
    SUM(a.goals_for) AS goals_for,
    SUM(a.goals_against) AS goals_against,
    SUM(a.goals_for) - SUM(a.goals_against) AS goals_difference
FROM team_appearances a
JOIN teams t ON t.team_id = a.team_id
WHERE tournament_id = COALESCE(tournament_id, tournament_id)
GROUP BY t.team_name;