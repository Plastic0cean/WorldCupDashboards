CREATE PROCEDURE MostBookingsByGames (tournamentid VARCHAR(10), how_many INT)

	WITH BookingsByGame AS (
	SELECT 
		m.tournament_id,
		b.match_id,
		m.home_team_id,
		t.team_name AS home_team_name,
		m.away_team_id,
		t2.team_name AS away_team_name,
		score(m.home_team_score, m.away_team_score) AS score,
		SUM(b.yellow_card) AS yellow_cards,
		SUM(b.red_card) AS red_cards
	FROM bookings b 
	JOIN matches m ON m.match_id = b.match_id
	JOIN teams t ON t.team_id = m.home_team_id 
	JOIN teams t2 ON t2.team_id = m.away_team_id
	JOIN tournaments tou ON tou.tournament_id = m.tournament_id
	WHERE m.tournament_id = COALESCE(tournamentid, m.tournament_id)
	GROUP BY 
		m.tournament_id,
		b.match_id,
		m.home_team_id,
		t.team_name,
		m.away_team_id,
		t2.team_name)
		
	SELECT * FROM BookingsByGame 
	WHERE yellow_cards + red_cards = (SELECT MAX(yellow_cards + red_cards) FROM BookingsByGame) LIMIT how_many;