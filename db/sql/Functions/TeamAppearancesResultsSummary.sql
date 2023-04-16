CREATE FUNCTION TeamAppearancesResultsSummary (@TeamId  NVARCHAR(100))
RETURNS TABLE 
AS 
RETURN 
SELECT 
	Result, 
	COUNT(*) AS [Number] 
FROM team_appearances 
WHERE team_id = @TeamId GROUP BY Result 
GO