CREATE PROCEDURE MatchEvents (matchid VARCHAR(10))

	WITH GoalEvents AS (
		SELECT 
			g.match_id,
			g.player_id,
			g.minute_regulation + g.minute_stoppage as minute,
			minute_label(g.minute_regulation, g.minute_stoppage) as minute_label,
			a.team_id,
			a.home_team,
			'goal' as type
		FROM goals g
		JOIN players p ON g.player_id = p.player_id 
		JOIN player_appearances pa ON pa.player_id = g.player_id AND pa.match_id = g.match_id

		JOIN team_appearances a ON g.match_id = a.match_id AND a.team_id = pa.team_id
		JOIN teams t ON a.team_id = t.team_id
		WHERE g.match_id = matchid),

	CardEvents AS (
		SELECT 
			b.match_id,
			b.player_id,
			b.minute_regulation + b.minute_stoppage as minute,
			minute_label(b.minute_regulation, b.minute_stoppage) as minute_label,
			a.team_id,
			a.home_team,
			CASE 
				WHEN b.yellow_card = 1 THEN 'yellow card' 
				WHEN b.red_card = 1 THEN 'red card' 
			END as type
		FROM bookings b 
		JOIN player_appearances p ON p.player_id = b.player_id AND p.match_id = b.match_id
		JOIN team_appearances a ON b.match_id = a.match_id AND a.team_id = p.team_id
		WHERE b.match_id = matchid),

	SubtitutionEvents AS (
		SELECT 
			s.match_id,
			s.player_id,
			minute_label(s.minute_regulation, s.minute_stoppage) as minute_label,
			s.minute_regulation + s.minute_stoppage AS minute,
			s.team_id,
			home_team,
			IF(s.going_off = 1, 'sub out', 'sub in') as type
		FROM substitutions s 
		JOIN team_appearances a ON s.match_id = a.match_id AND s.team_id = a.team_id
		WHERE s.match_id = matchid),

	AllEvents AS (
		SELECT * FROM GoalEvents
		UNION ALL 
		SELECT * FROM CardEvents
		UNION ALL 
		SELECT * FROM SubtitutionEvents)

	SELECT 
		e.match_id, 
		e.player_id, 
		parse_name (p.given_name, p.family_name) AS player_name,
		e.minute_label, 
		e.team_id, 
		t.team_name,
		e.home_team, 
		e.type 
	FROM AllEvents e
	JOIN teams t ON e.team_id = t.team_id
	JOIN players p ON e.player_id = p.player_id 
	ORDER BY minute;