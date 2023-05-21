CREATE FUNCTION PlayerBasicStatistics (@player_id VARCHAR(10))
RETURNS @T TABLE (
	goals INT,
	matches INT, 
	red_cards INT,
	yellow_cards INT
)
AS BEGIN 
	
	DECLARE @goals INT,
			@appearances INT,
			@red_cards INT,
			@yellow_cards INT
			
	SELECT @goals = dbo.NumberOfPlayerGoals(@player_id)
	SELECT @appearances = dbo.NumberOfPlayerAppearances(@player_id)

	SELECT 
		@yellow_cards = COALESCE(SUM(CAST(yellow_card AS INT)), 0),
		@red_cards = COALESCE(SUM(CAST(red_card AS INT)), 0)
	FROM bookings WHERE player_id = @player_id

	INSERT INTO @T VALUES (@goals, @appearances, @red_cards, @yellow_cards)
	RETURN
END;