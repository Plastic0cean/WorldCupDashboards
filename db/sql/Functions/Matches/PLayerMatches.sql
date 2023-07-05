CREATE FUNCTION PlayerMatches (@player_id VARCHAR(20))
RETURNS TABLE
AS RETURN 
WITH player_matches AS (
	SELECT 
	m.home_team_id,
	m.home_team_name,
	m.away_team_id,
	m.away_team_name,
	m.score,
	p.match_date,
	starter,
	p.tournament_id,
	SUM(CAST(ISNULL(yellow_card, 0) AS INT)) AS yellow_cards,
	SUM(CAST(ISNULL(red_card, 0) AS INT)) AS red_cards,
	s.minute_regulation,
	CASE 
		WHEN extra_time = 0 THEN 90
		ELSE 120
	END AS possible_minutes
	FROM player_appearances p 
	JOIN matches m ON p.match_id = m.match_id
	LEFT JOIN bookings b ON b.match_id = p.match_id AND b.player_id = p.player_id
	LEFT JOIN substitutions s ON p.player_id = s.player_id AND m.match_Id = s.match_id
	WHERE p.player_id = @player_id
	GROUP BY 
		m.home_team_id, 
		s.minute_regulation, 
		m.home_team_name, 
		starter, 
		m.away_team_id, 
		m.away_team_name, 
		p.match_date, 
		m.score, 
		extra_time,
		p.tournament_id
)

	SELECT 
		*, 
		CASE 
			WHEN starter = '1' THEN COALESCE(minute_regulation, possible_minutes)
			WHEN starter = '0' THEN possible_minutes - CAST(minute_regulation AS INT)
		END AS minutes_played
	FROM player_matches