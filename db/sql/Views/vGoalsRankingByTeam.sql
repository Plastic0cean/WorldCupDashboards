CREATE VIEW [vGoalsRankingByTeam] AS 

WITH GoalsByTeam AS (
		SELECT 
			TeamId AS team_id,
			[TeamName] AS team_name,
			COUNT(*) AS goals_scored
		FROM [Reports].[Goals]
		GROUP BY [TeamName], [TeamId])
	SELECT 
		RANK() OVER (ORDER BY goals_scored DESC) AS [Position],
		team_id,
		team_name,
		goals_scored
	FROM [GoalsByTeam]
