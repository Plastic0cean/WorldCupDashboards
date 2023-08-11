CREATE PROCEDURE GoalsByMinutes (tournamentid VARCHAR(10))
	SELECT 
		minute_regulation AS minute
	FROM goals g
    JOIN matches m ON m.match_id = g.match_id
	WHERE tournament_id = COALESCE(tournamentid, tournament_id);
