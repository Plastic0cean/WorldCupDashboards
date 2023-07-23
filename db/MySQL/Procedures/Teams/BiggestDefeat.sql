DELIMITER //
CREATE PROCEDURE BiggestDefeat (teamid VARCHAR(10))
BEGIN
	SELECT 
		a.tournament_id, 
		tour.tournament_name, 
		a.opponent_id, 
		t.team_name as opponent_name, 
		m.match_date, 
		score(a.goals_for, a.goals_against) as score
	FROM team_appearances a
	JOIN tournaments tour ON tour.tournament_id = a.tournament_id
	JOIN teams t ON t.team_id = a.opponent_id
	JOIN matches m ON a.match_id = m.match_id
	WHERE a.team_id = teamid AND a.lose=1 AND goals_against - goals_for  = (SELECT MAX(goals_against - goals_for) FROM team_appearances WHERE team_id = teamid AND Lose=1);
END //
DELIMITER ; 