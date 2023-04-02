CREATE FUNCTION PlayerGoalsByMinutes (@playerId VARCHAR(20))
RETURNS TABLE AS RETURN 

	SELECT 
		minuteRegulation AS [minute],
		COUNT(*) AS number_of_goals
	FROM Reports.goals 
	WHERE PlayerId = @playerId 
	GROUP BY minuteRegulation, matchPeriod 
