CREATE PROCEDURE TopScorers (teamid VARCHAR(10), how_many INT)
	SELECT 
		g.player_id,
		parse_name(p.given_name, p.family_name) AS player_name,
		COUNT(*) AS goals_number
	FROM goals g 
	JOIN players p ON g.player_id = p.player_id
	WHERE player_team_id = teamid
	GROUP BY g.player_id, p.given_name, p.family_name
    ORDER BY goals_number DESC
    LIMIT how_many;