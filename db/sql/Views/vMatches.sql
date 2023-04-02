CREATE VIEW [vMatches] AS 
SELECT 
	home_team AS [HomeTeam],
	away_team AS [AwayTeam],
	TRY_CONVERT(int, home_score) AS [HomeScore],
	TRY_CONVERT(NUMERIC(10, 2), home_xg ) AS HomeXG,
	TRY_CONVERT(int, home_penalty) AS HomePanelty,
	TRY_CONVERT(int, away_score) AS AwayScore,
	TRY_CONVERT(NUMERIC(10, 2), away_xg ) AS AwayXG,
	TRY_CONVERT(int, away_penalty) AS AwayPenalty,
	home_manager AS HomeManager,
	home_captain AS HomeCaptain,
	away_manager AS AwayManager,
	away_captain AS AwayCaptain,
	Attendance,
	Venue,
	Officials,
	Round,
	CAST([Date] as Date) AS MatchDate,
	Score,
	Referee,
	Notes,
	Host,
	[Year],
	home_goal AS HomeGoal,
	away_goal AS AwayGoal,
	home_goal_long AS HomeGoalLong,
	away_goal_long AS AwayGoalLong,
	home_own_goal As HomeOwnGoal,
	away_own_goal AS AwayOwnGoal,
	home_penalty_goal AS HomePenaltyGoal,
	away_penalty_goal AS AwayPenaltyGoal,
	Home_Penalty_Miss_Long AS HomePenaltyMissLong,
	Away_Penalty_Miss_Long AS AwayPenaltyMissLong,
	home_penalty_shootout_goal_long AS homePenaltyShootoutGoalLong,
	away_penalty_shootout_goal_long AS awayPenaltyShootoutGoalLong,
	home_penalty_shootout_miss_long AS homePenaltyShootoutMissLong,
	away_penalty_shootout_miss_long AS awayPenaltyShootoutMissLong,
	home_red_card AS HomeRedCard,
	away_red_card,
	home_yellow_red_card,
	away_yellow_red_card,
	home_yellow_card_long,
	away_yellow_card_long,
	home_substitute_in_long,
	away_substitute_in_long
FROM [matches_1930_2022]