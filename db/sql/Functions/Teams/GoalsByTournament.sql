ALter FUNCTION GoalsByTournament (@team_id VARCHAR(20))
RETURNS TABLE
AS RETURN 

    SELECT 
        tournament_id AS tournament_name,
        SUM(CAST(goals_for AS INT)) AS number_of_goals
    FROM team_appearances 
    WHERE team_id = @team_id
    GROUP BY tournament_id 
    HAVING SUM(CAST(goals_for AS INT))>0 