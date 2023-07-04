CREATE FUNCTION MostBookingsByGames(@tournament_id VARCHAR(100)=NULL)
RETURNS TABLE AS RETURN

WITH BookingsByGame AS (
SELECT 
	tournament_id, 
	match_id, 
	match_name,	
	SUM(CAST(yellow_card AS INT)) yellow_cards,
	SUM(CAST(red_card AS INT)) red_cards,
	SUM(CAST(yellow_card AS INT)) + SUM(CAST(red_card AS INT)) AS cards_overall
FROM bookings
WHERE tournament_id = COALESCE(@tournament_id, tournament_id)
GROUP BY tournament_id, match_id, match_name)

SELECT TOP 1 * FROM BookingsByGame WHERE cards_overall = (SELECT MAX(cards_overall) FROM BookingsByGame)