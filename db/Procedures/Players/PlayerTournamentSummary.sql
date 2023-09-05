CREATE PROCEDURE PlayerTournamentSummary (playerid VARCHAR(10))
	WITH games AS (
		SELECT 
			tournament_id, 
			COUNT(a.match_id) AS number_of_matches
		FROM player_appearances a 
        JOIN matches m ON m.match_id = a.match_id
		WHERE player_id = playerid
		GROUP BY tournament_id
	),
	goal AS (
		SELECT 
			tournament_id, 
			COUNT(goal_id) AS number_of_goals
		FROM goals g 
		JOIN matches m ON m.match_id = g.match_id
		WHERE player_id = playerid
		GROUP BY tournament_id
	),
	cards AS (
		SELECT 
			tournament_id,
			SUM(yellow_card) AS yellow_cards,
			SUM(red_card) AS red_cards
		FROM bookings b 
        JOIN matches m ON b.match_id = m.match_id
		WHERE player_id = playerid
		GROUP BY tournament_id
	)

	SELECT 
		g1.tournament_id,
		tournament_name(t.year, t.host_country) AS tournament_name,
		number_of_matches, 
		COALESCE(number_of_goals, 0) AS number_of_goals,
		COALESCE(yellow_cards, 0) AS yellow_cards,
		COALESCE(red_cards, 0) AS red_cards
	FROM games g1
	LEFT JOIN goal g2 ON g1.tournament_id = g2.tournament_id
	LEFT JOIN cards c ON g1.tournament_id = c.tournament_id
    JOIN tournaments t ON g1.tournament_id = t.tournament_id;