BEGIN TRY 

BEGIN TRANSACTION 
--Data transformation 
--1. Create [Teams] table 
SELECT
    team_id AS TeamId,
    team_name AS TeamName,
    team_code AS TeamCode,
    federation_name AS FederationName ,
    region_name AS RegionName,
    confederation_id AS ConfederationId 
INTO Reports.Teams
FROM teams 

--2. Create [Goals] table
UPDATE goals SET given_name = NULL WHERE given_name = 'not applicable'

SELECT 
	goal_id AS GoalId, 
	tournament_id AS TournamentId, 
	match_id AS MatchId, 
	match_name AS MatchName, 
	CAST(match_date	AS Date) AS MatchDate, 
	stage_name AS StageName,
	group_name AS GroupName,
	team_id AS TeamId,
	team_name AS TeamName,
	team_code AS TeamCode,
	CAST(home_team AS Int) AS HomeTeam,
	CAST(away_team AS Int) AS AwayTeam,
	player_id AS PlayerId,
	family_name AS FamilyName,
	given_name AS GivenName,
	CAST(shirt_number AS Int) AS ShirtNumber, 
	player_team_id, 
	player_team_name, 
	player_team_code, 
	minute_label, 
	CAST(minute_regulation AS Int) AS MinuteRegulation,
	CAST(minute_stoppage AS Int) AS MinuteStoppage,
	match_period AS MatchPeriod,
	CAST(own_goal AS BIT) AS OwnGoal,
	CAST(penalty AS Bit) AS Penalty
INTO [Reports].[Goals]
FROM goals

--3. Create Players table 
UPDATE players SET given_name = NULL WHERE given_name = 'not applicable'
SELECT * INTO Reports.Players FROM players

--4. Update Stadiums table 
ALTER TABLE stadiums ADD coordinates_lat float 
ALTER TABLE stadiums ADD coordinates_long float 
UPDATE stadiums SET stadium_wikipedia_link = 'https://en.wikipedia.org/wiki/Arena_Independ%C3%AAncia' WHERE stadium_id = 'S-007'



COMMIT TRANSACTION
END TRY 

BEGIN CATCH 
PRINT ERROR_MESSAGE()
ROLLBACK TRANSACTION 
END CATCH 



