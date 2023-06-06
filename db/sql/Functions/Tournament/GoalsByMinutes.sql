USE [WorldCupStats]
GO 

CREATE FUNCTION GoalsByMinutes(@tournament_id VARCHAR(10)=NULL)
RETURNS TABLE 
AS RETURN 
	SELECT 
		CAST(minute_regulation as INT) as [minute]
	FROM goals 
	WHERE tournament_id = COALESCE(@tournament_id, tournament_id)
GO		

