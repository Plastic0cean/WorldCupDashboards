CREATE PROCEDURE BiggestDefeat (teamid VARCHAR(10))
	SELECT 
		a.match_id,
		a.tournament_id, 
		tour.tournament_name, 
		m.home_team_id, 
		m.away_team_id,
		t.team_name AS home_team_name,
		t2.team_name as away_team_name, 
		m.match_date, 
		score(m.home_team_score, m.away_team_score) as score
	FROM team_appearances a
	JOIN tournaments tour ON tour.tournament_id = a.tournament_id
	JOIN matches m ON a.match_id = m.match_id
	JOIN teams t ON t.team_id = m.home_team_id
	JOIN teams t2 ON t2.team_id = m.away_team_id
	WHERE a.team_id = teamid AND a.lose=1 AND goals_against - goals_for  = (SELECT MAX(goals_against - goals_for) FROM team_appearances WHERE team_id = teamid AND Lose=1);