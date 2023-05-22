CREATE FUNCTION TeamScorers (@TeamId VARCHAR(2000))
RETURNS TABLE 
AS RETURN 
	SELECT 
		[PlayerId] AS player_id, 
		LTRIM(CONCAT(GivenName, ' ', familyName)) AS player_name, 
		COUNT(*) AS goals_number
	FROM [Reports].[Goals]
	WHERE [TeamId] = @TeamId
	GROUP BY [PlayerId], [FamilyName], [GivenName]
GO

