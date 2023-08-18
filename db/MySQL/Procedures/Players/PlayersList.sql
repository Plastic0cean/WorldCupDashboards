CREATE PROCEDURE PlayersList ()
	WITH all_players AS (
		SELECT 
		ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY player_id) AS player_number,
		player_id,
		team_id
		FROM squads)
	SELECT 
		a.player_id,
		parse_name(p.given_name, p.family_name) as name,
		COALESCE(p.given_name, '') AS given_name,
		p.family_name,
		p.position,
		a.team_id,
		t.team_name
	FROM all_players a
	JOIN players p ON a.player_id = p.player_id 
	JOIN teams t ON a.team_id = t.team_id
	WHERE player_number = 1 AND a.player_id IN (SELECT player_id FROM player_appearances)
    ORDER BY name ASC;