CREATE FUNCTION NumberOfPlayerAppearances (@player_id VARCHAR(10))
RETURNS INT
AS BEGIN
	DECLARE @number_of_appearances INT 
	SELECT @number_of_appearances = COUNT(*) FROM player_appearances WHERE player_id = @player_id

	RETURN @number_of_appearances
END

GO