CREATE PROCEDURE PositionsOnTournaments (teamid VARCHAR(10))
SELECT 
    q.tournament_id, 
    tournament_name(t.year, t.host_country) AS tournament_name,
	q.count_matches, 
    performance,
    g.position AS group_position
FROM qualified_teams q 
JOIN tournaments t ON t.tournament_id = q.tournament_id
LEFT JOIN group_standings g 
ON g.tournament_id = q.tournament_id AND q.team_id = g.team_id
WHERE q.team_id = teamid
ORDER BY t.year ASC;