CREATE PROCEDURE MinutesPlayedByPlayers (teamid VARCHAR(10), how_many INT)
    SELECT 
	    a.player_id,
        parse_name(p.given_name, p.family_name) AS player_name,
        minutes_played
    FROM player_appearances a 
    JOIN players p ON a.player_id = p.player_id
    WHERE a.team_id = teamid
    ORDER BY minutes_played DESC
    LIMIT how_many;