CREATE FUNCTION TeamsPowerRanking (@tournament_id VARCHAR(10))
RETURNS @T TABLE (team_id VARCHAR(10), team_name VARCHAR(200), points INT)
AS
BEGIN 


IF @tournament_id IS NULL 
	INSERT INTO @T
	SELECT 
		team_id, 
		team_name, 
		SUM(3*CAST(win AS INT) + CAST(draw AS INT)) as points
	FROM team_appearances
	GROUP BY team_id, team_name

ELSE 
	INSERT INTO @T
		SELECT 
		team_id, 
		team_name, 
		SUM(3*CAST(win AS INT) + CAST(draw AS INT)) as points
	FROM team_appearances
	WHERE tournament_id = @tournament_id 
	GROUP BY team_id, team_name

RETURN 
END;
GO 