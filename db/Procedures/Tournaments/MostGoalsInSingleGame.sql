CREATE PROCEDURE MostGoalsInSingleGame (tournamentid VARCHAR(10))
	WITH MatchResults AS (
	SELECT 
		m.tournament_id,
		m.match_id,
		m.home_team_id,
		t.team_name AS home_team_name,
		m.away_team_id,
		t2.team_name AS away_team_name,
		score(m.home_team_score, m.away_team_score) AS score,
		m.match_date,
		m.home_team_score + m.away_team_score AS number_of_goals
	FROM matches m
	JOIN teams t ON t.team_id = m.home_team_id 
	JOIN teams t2 ON t2.team_id = m.away_team_id
	WHERE tournament_id = COALESCE(tournamentid, tournament_id))

	SELECT 
		tournament_id,
		match_id,
		home_team_id,
		home_team_name,
		away_team_id,
		away_team_name,
		score,
		match_date
	FROM MatchResults 
	WHERE number_of_goals = (SELECT MAX(number_of_goals) FROM MatchResults) LIMIT 1;