CREATE FUNCTION TeamAppearancesResultsSummary (@TeamName NVARCHAR(100))
RETURNS TABLE 
AS 
RETURN 
SELECT Result, COUNT(*) AS [Number] FROM team_appearances WHERE team_name = @TeamName GROUP BY Result 
