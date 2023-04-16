from Db.DbConnection import conn

def get_all_team_names():
    with conn:
        names = conn.execute("SELECT team_id, team_name FROM Teams", True)
    return [name for name in names]

def get_goal_ranking_by_team(team_id: str):
    with conn: 
        query = f"SELECT * FROM vGoalsRankingByTeam WHERE team_id = '{team_id}'"
        result = conn.execute(query, get_results=True)
    if result:
        return result[0]

def get_biggest_win_by_team(team_id: str):
    with conn: 
        result = conn.execute(f"SELECT * FROM BiggestWinOfTeam('{team_id}')", get_results=True)
    return result

def get_biggest_defeat_by_team(team_id: str):
    with conn: 
        result = conn.execute(f"SELECT * FROM BiggestDefeatOfTeam('{team_id}')", get_results=True)
    return result

def get_top_scorers(team_id: str, how_many: int=None):
    top = ""
    if how_many:
        top = f"TOP {how_many}"
    with conn:
        return conn.execute(
            f"SELECT {top} * FROM TeamScorers ('{team_id}') ORDER BY GoalsNumber DESC", 
            get_results=True)
    
def get_team_matches_summary(team_id: str):
    with conn:
        return conn.select_as_dict(f"SELECT * FROM TeamAppearancesResultsSummary('{team_id}')")