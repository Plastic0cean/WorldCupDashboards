CREATE PROCEDURE MatchResult (matchid VARCHAR(10))

SELECT 
	match_id,
	m.home_team_id,
	t.team_name AS home_team_name,
	m.match_date,
	m.away_team_id,
	t2.team_name AS away_team_name,
	score(m.home_team_score, m.away_team_score) as score
FROM matches m 
JOIN teams t ON m.home_team_id  = t.team_id
JOIN teams t2 ON m.away_team_id = t2.team_id
WHERE match_id = matchid
ORDER BY match_date ASC;