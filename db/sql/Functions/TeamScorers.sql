CREATE FUNCTION TeamScorers (@Team VARCHAR(2000))
RETURNS TABLE 
AS RETURN 
	SELECT 
		[PlayerId], 
		[FamilyName], 
		[GivenName], 
		COUNT(*) AS GoalsNumber
	FROM [Reports].[Goals]
	WHERE [TeamName] = @Team
	GROUP BY [PlayerId], [FamilyName], [GivenName]
GO

