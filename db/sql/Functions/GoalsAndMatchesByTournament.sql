CREATE FUNCTION GoalsAndMatchesByTournament()
RETURNS TABLE 
RETURN 

	SELECT 
		m.tournament_id, 
		t.[year],
		t.host_country AS country,
		COUNT(*) AS matches,
		SUM(CAST(home_team_score AS INT) + CAST(away_team_score AS INT)) AS goals
	FROM matches m 
	JOIN tournaments t ON m.tournament_id = t.tournament_id
	GROUP BY m.tournament_id,	t.[year], t.host_country 
