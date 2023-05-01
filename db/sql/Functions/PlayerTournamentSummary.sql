CREATE FUNCTION PlayerTournamentSummary (@player_id VARCHAR(20))
RETURNS TABLE 
AS RETURN 
	WITH games AS (
		SELECT 
			tournament_id, 
			tournament_name,
			COUNT(match_id) AS number_of_matches
		FROM player_appearances
		WHERE player_id = @player_id
		GROUP BY 
		tournament_id, 
		tournament_name
	),
	goal AS (
		SELECT 
			tournament_id, 
			COUNT(goal_id) AS number_of_goals
		FROM goals 
		WHERE player_id = @player_id
		GROUP BY tournament_id
	),
	cards AS (
		SELECT 
			tournament_id,
			SUM(CAST(yellow_card AS Int)) AS yellow_cards,
			SUM(CAST(red_card AS Int)) AS red_cards
		FROM bookings
		WHERE player_id = @player_id
		GROUP BY tournament_id
	)

	SELECT 
		g1.tournament_id,
		g1.tournament_name AS tournament, 
		number_of_matches, 
		COALESCE(number_of_goals, 0) AS number_of_goals,
		COALESCE(yellow_cards, 0) AS yellow_cards,
		COALESCE(red_cards, 0) AS red_cards
	FROM games g1
	LEFT JOIN goal g2 ON g1.tournament_id = g2.tournament_id
	LEFT JOIN cards c ON g1.tournament_id = c.tournament_id
