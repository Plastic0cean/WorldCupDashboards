CREATE FUNCTION TeamPositionOnTournaments (@team_id VARCHAR(100)) 
RETURNS TABLE 
AS RETURN 
--Position on every tournament 
WITH groupes AS (
	SELECT 
		MAX(CAST(stage_number as int)) OVER (PARTITION BY tournament_name) AS max_stage_number,
		*
	FROM group_standings 
	WHERE team_id=@team_id),
BestGroupResultByTournament AS (
	SELECT * FROM groupes WHERE max_stage_number = stage_number)
SELECT 
	q.tournament_id, 
	q.tournament_name, 
	q.team_name, 
	q.count_matches, 
	COALESCE(s.position,
	CASE 
		WHEN q.performance = 'group stage' THEN CONCAT(g.stage_name, ' (', g.position, ' position)')
		ELSE q.performance
	END) AS position
FROM qualified_teams q 
FULL OUTER JOIN BestGroupResultByTournament g ON g.tournament_id = q.tournament_id AND g.team_id = q.team_id
LEFT JOIN tournament_standings s ON q.tournament_id = s.tournament_id AND q.team_id = s.team_id
WHERE q.team_id = @team_id
