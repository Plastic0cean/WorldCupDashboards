CREATE PROCEDURE SquadsByMatch (matchid VARCHAR(10), hometeam BOOLEAN)
SELECT 
	a.player_id,
	parse_name (p.given_name, p.family_name) AS player_name,
	a.team_id,
	a.position,
	a.shirt_number,
    True AS home_team
FROM player_appearances a
JOIN players p ON a.player_id = p.player_id
JOIN matches m ON m.match_id = a.match_id AND a.team_id = IF(hometeam, m.home_team_id, m.away_team_id)
WHERE a.match_id = matchid AND starter = True
ORDER BY a.shirt_number;