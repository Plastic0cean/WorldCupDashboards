CREATE PROCEDURE ResultsSummary (teamid VARCHAR(10))
	SELECT 
		SUM(win) AS wins,
		SUM(lose) AS loses,
		SUM(draw) AS draws
	FROM team_appearances 
	WHERE team_id = teamid;