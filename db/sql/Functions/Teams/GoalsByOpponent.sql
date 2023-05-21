CREATE FUNCTION GoalsByOpponent (@team_id VARCHAR(20))
RETURNS TABLE
AS RETURN 

    SELECT 
        opponent_name,
        SUM(CAST(goals_for AS INT)) AS number_of_goals
    FROM team_appearances 
    WHERE team_id = @team_id
    GROUP BY opponent_name
    HAVING SUM(CAST(goals_for AS INT))>0 