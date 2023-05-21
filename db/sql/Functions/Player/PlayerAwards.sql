CREATE FUNCTION PlayerAwards(@player_id VARCHAR(10))
RETURNS TABLE AS 
RETURN 
	SELECT 
		w.award_name AS [name], 
		award_description AS [description], 
		w.tournament_id, 
		t.[year],
		t.[host_country] AS [country]
	FROM award_winners w
	JOIN awards a ON a.award_id = w.award_id
	JOIN tournaments t ON w.tournament_id = t.tournament_id
	WHERE player_id = @player_id