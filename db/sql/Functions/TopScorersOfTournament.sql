CREATE FUNCTION TopScorersOfTournament (@tournament_id VARCHAR(10)=NULL)
RETURNS TABLE AS RETURN

	SELECT 
		player_id, 
		LTRIM(CONCAT(given_name, ' ', family_name)) as player_name, 
		player_team_id AS team_id, 
		player_team_name AS team, 
		COUNT(*) AS goals 
	FROM goals
	WHERE tournament_id = COALESCE(@tournament_id, tournament_id)
	GROUP BY player_id, given_name, family_name, player_team_id, player_team_name  
GO