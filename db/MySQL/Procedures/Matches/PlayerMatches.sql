CREATE PROCEDURE PlayerMatches (playerid VARCHAR(20))
	SELECT 
		m.tournament_id,
		m.match_id, 
		m.home_team_id,
		t.team_name AS home_team_name,
		m.away_team_id,
		t2.team_name AS away_team_name,
		score(m.home_team_score, m.away_team_score) AS score,
		m.match_date,
		a.minutes_played,
		SUM(b.yellow_card) AS yellow_cards,
		SUM(b.red_card) AS red_cards
	FROM matches m 
	JOIN teams t ON m.home_team_id = t.team_id 
	JOIN teams t2 ON m.away_team_id = t2.team_id 
	JOIN player_appearances a ON a.match_id = m.match_id
	LEFT JOIN bookings b ON b.match_id = m.match_id AND b.player_id = a.player_id
	WHERE a.player_id = playerid
	GROUP BY 
		m.tournament_id,
		m.match_id, 
		m.home_team_id, 
		t.team_name,
		m.away_team_id,	
		t2.team_name,
		m.home_team_score, 
		m.away_team_score,
		m.match_date,
		a.minutes_played;