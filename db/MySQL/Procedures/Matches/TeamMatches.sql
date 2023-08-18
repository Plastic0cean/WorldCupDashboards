CREATE PROCEDURE TeamMatches (teamid VARCHAR(10))
	SELECT 
		m.tournament_id,
		m.match_id, 
		m.home_team_id,
		t.team_name AS home_team_name,
		m.away_team_id,
		t2.team_name AS away_team_name,
		score(m.home_team_score, m.away_team_score) AS score,
		m.match_date
FROM matches m 
JOIN teams t ON m.home_team_id = t.team_id 
JOIN teams t2 ON m.away_team_id = t2.team_id 
JOIN team_appearances a ON a.match_id = m.match_id
WHERE a.team_id = teamid
ORDER BY m.match_date ASC;
