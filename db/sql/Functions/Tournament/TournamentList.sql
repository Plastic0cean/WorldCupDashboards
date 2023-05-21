CREATE FUNCTION TournamentList()
RETURNS TABLE AS RETURN
	SELECT tournament_id, tournament_name, year, host_country, winner 
	FROM tournaments