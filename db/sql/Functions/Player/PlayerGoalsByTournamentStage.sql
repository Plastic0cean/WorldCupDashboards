CREATE FUNCTION PlayerGoalsByTournamentStage(@playerId VARCHAR(20))
RETURNS TABLE AS RETURN 
	
	SELECT 
		StageName as stage_name, 
		COUNT(*) as number_of_goals 
	FROM Reports.Goals 
	WHERE PlayerId = @playerId
	GROUP BY StageName