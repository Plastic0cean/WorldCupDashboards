CREATE PROCEDURE BiggestWin (teamid VARCHAR(10))
	SELECT 
		a.tournament_id, 
		a.match_id,
		m.home_team_id, 
		t.team_name AS home_team_name,
		m.away_team_id,
		t2.team_name as away_team_name, 
		score(m.home_team_score, m.away_team_score) as score,
		m.match_date
	FROM team_appearances a
	JOIN matches m ON a.match_id = m.match_id
	JOIN teams t ON t.team_id = m.home_team_id
	JOIN teams t2 ON t2.team_id = m.away_team_id
	WHERE a.team_id = teamid AND a.win = 1 AND goals_for - goals_against = (SELECT MAX(goals_for - goals_against) FROM team_appearances WHERE team_id = teamid AND win = 1);