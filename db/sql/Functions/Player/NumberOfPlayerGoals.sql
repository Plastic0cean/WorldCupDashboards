CREATE FUNCTION NumberOfPlayerGoals (@player_id VARCHAR(10))
RETURNS INT
AS BEGIN
	DECLARE @number_of_goals INT 
	SELECT @number_of_goals = COUNT(*) FROM goals WHERE player_id = @player_id

	RETURN @number_of_goals
END
GO
