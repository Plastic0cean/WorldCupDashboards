CREATE PROCEDURE MostGoalsInSingleGame (playerid VARCHAR(10))
	WITH MatchResults AS (
	SELECT 
		m.tournament_id,
		m.match_id,
		m.match_date,
		m.home_team_id,
		t.team_name AS home_team_name,
		m.away_team_id,
		t2.team_name AS away_team_name,
		score(m.home_team_score, m.away_team_score) AS score,
		m.home_team_score + m.away_team_score AS number_of_goals
	FROM matches m
	JOIN teams t ON t.team_id = m.home_team_id 
	JOIN teams t2 ON t2.team_id = m.away_team_id
	WHERE tournament_id = COALESCE(tournament_id, tournament_id))

	SELECT * FROM MatchResults WHERE number_of_goals = (SELECT MAX(number_of_goals) FROM MatchResults) LIMIT 1;