DELIMITER //
CREATE PROCEDURE MatchesResultsByTeam (teamid VARCHAR(10))
BEGIN
	SELECT 
		a.lose, 
		a.draw,
		a.win,
		m.match_date,
		a.match_id,
		t.team_name AS opponent_name,
		score(a.goals_for, a.goals_against) as score,
		a.goals_for - a.goals_against AS goal_differential
    FROM team_appearances a 
    JOIN matches m ON m.match_id = a.match_id 
    JOIN teams t ON t.team_id = a.opponent_id
    WHERE team_id = teamid;
END //
DELIMITER ;