CREATE PROCEDURE MatchesOfTeam (teamid VARCHAR(10))
	SELECT 
		a.match_id,
		t.team_name AS opponent_name,
		a.win,
		a.lose, 
		a.draw,
		score(a.goals_for, a.goals_against) AS score,
		a.goals_for - a.goals_against AS goal_differential
	FROM team_appearances a
	JOIN teams t ON a.opponent_id = t.team_id
    WHERE a.team_id = teamid;