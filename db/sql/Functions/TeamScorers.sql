CREATE FUNCTION TeamScorers (@TeamId VARCHAR(2000))
RETURNS TABLE 
AS RETURN 
	SELECT 
		[PlayerId], 
		[FamilyName], 
		[GivenName], 
		COUNT(*) AS GoalsNumber
	FROM [Reports].[Goals]
	WHERE [TeamId] = @TeamId
	GROUP BY [PlayerId], [FamilyName], [GivenName]
GO

