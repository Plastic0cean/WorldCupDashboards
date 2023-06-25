CREATE FUNCTION MatchEvents(@match_id VARCHAR(10))
RETURNS TABLE AS RETURN 
SELECT 
	match_id,
	player_id,
	CONCAT_WS(' ', family_name, given_name) as [player_name],
	'goal' as [type],
	minute_label,
	CAST(minute_regulation as int) + CAST(minute_stoppage as int) as [minute],
	team_id
FROM goals WHERE [match_id] = @match_id
UNION ALL
SELECT 
	match_id,
	player_id,
	CONCAT_WS(' ', family_name, given_name) as [player_name],
	CASE 
		WHEN yellow_card = '1' THEN 'yellow card' 
		WHEN red_card = '1' THEN 'red card' 
	END as [type],
	minute_label,
	CAST(minute_regulation as int) + CAST(minute_stoppage as int) as [minute],
	team_id
FROM bookings WHERE [match_id] = @match_id
UNION ALL

SELECT 
	match_id,
	player_id,
	CONCAT_WS(' ', family_name, given_name) as [player_name],
	IIF(going_off = '1', 'sub out', 'sub in') as [type],
	minute_label,
	CAST(minute_regulation as int) + CAST(minute_stoppage as int) as [minute],
	team_id
FROM substitutions WHERE [match_id] = @match_id
GO 

