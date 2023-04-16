CREATE VIEW vLeagueTable  AS 
	SELECT 
		team_name,
		SUM(CAST(win AS INT)) AS wins,
		SUM(CAST(lose AS INT)) AS loses,
		SUM(CAST(draw AS INT)) AS draws,
		3 *SUM(CAST(win AS INT)) + SUM(CAST(draw AS INT)) AS points
	FROM team_appearances 
	GROUP BY team_name
GO