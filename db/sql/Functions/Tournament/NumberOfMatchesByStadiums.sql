CREATE FUNCTION NumberOfMatchesByStadiums (@tournament_id VARCHAR(10) = NULL)
RETURNS TABLE AS 
RETURN 

	SELECT 
		m.tournament_id,
		s.stadium_name, 
		s.city_name,
		s.country_name,
		s.coordinates_lat,
		s.coordinates_long,
		COUNT(m.match_id) AS number_of_games
	FROM Matches m 
	JOIN tournaments t ON m.tournament_id = t.tournament_id
	JOIN stadiums s ON m.stadium_id = s.stadium_id
	WHERE m.tournament_id = COALESCE(@tournament_id, m.tournament_id)
	GROUP BY m.tournament_id,
			 s.stadium_name, 
			 s.city_name,
			 s.country_name,
			 s.coordinates_lat,
			 s.coordinates_long
GO 


