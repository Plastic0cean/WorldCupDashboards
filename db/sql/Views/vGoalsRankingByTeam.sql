
CREATE VIEW [vGoalsRankingByTeam] AS 

WITH GoalsByTeam AS (
		SELECT 
			[TeamName],
			COUNT(*) AS [GoalsScored]
		FROM [Reports].[Goals]
		GROUP BY [TeamName])
	SELECT 
		RANK() OVER (ORDER BY [GoalsScored] DESC) AS [Position],
		[TeamName],
		[GoalsScored]
	FROM [GoalsByTeam]
