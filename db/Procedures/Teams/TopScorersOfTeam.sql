CREATE PROCEDURE TopScorersOfTeam (teamid VARCHAR(10), how_many INT)
	SELECT 
		g.player_id,
		parse_name(p.given_name, p.family_name) AS player_name,
        g.player_team_id AS team_id,
        t.team_name AS team_name,
		COUNT(*) AS goals
	FROM goals g 
	JOIN players p ON g.player_id = p.player_id
    JOIN teams t ON g.player_team_id = t.team_id
	WHERE player_team_id = teamid
	GROUP BY g.player_id, p.given_name, p.family_name, g.player_team_id, t.team_name
    ORDER BY goals DESC
    LIMIT how_many;