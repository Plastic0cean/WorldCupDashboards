DELIMITER //

CREATE PROCEDURE PlayerAwards (playerid VARCHAR(10))
	SELECT 
		award_name,
		award_description,
		tournament_name(t.year, t.host_country) AS tournament_name
	FROM award_winners w
	JOIN awards a ON a.award_id = w.award_id
	JOIN tournaments t ON w.tournament_id = t.tournament_id
	WHERE player_id = playerid
	ORDER BY t.year;
END //
DELIMITER ;