CREATE PROCEDURE GamesAsStarterOrSubstitute (playerid VARCHAR(10))
    SELECT
        SUM(starter) AS starter,
        SUM(substitute) AS substitute
    FROM player_appearances 
    WHERE player_id = playerid;