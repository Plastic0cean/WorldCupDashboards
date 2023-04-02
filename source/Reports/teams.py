from Db.DbConnection import conn

def get_all_team_names():
    with conn:
        names = conn.execute("SELECT TeamName FROM [Reports].[Teams]", True)
    return [name[0] for name in names]

def get_goal_ranking_by_team(team_name: str):
    with conn: 
        query = f"SELECT * FROM vGoalsRankingByTeam WHERE TeamName = '{team_name}'"
        result = conn.execute(query, get_results=True)
    if result:
        return result[0]

def get_biggest_win_by_team(team_name: str):
    with conn: 
        result = conn.execute(f"SELECT * FROM BiggestWinOfTeam('{team_name}')", get_results=True)
    return result

def get_biggest_defeat_by_team(team_name: str):
    with conn: 
        result = conn.execute(f"SELECT * FROM BiggestDefeatOfTeam('{team_name}')", get_results=True)
    return result

def get_top_scorers(team_name: str, how_many: int=None):
    top = ""
    if how_many:
        top = f"TOP {how_many}"
    with conn:
        return conn.execute(
            f"SELECT {top} * FROM TeamScorers ('{team_name}') ORDER BY GoalsNumber DESC", 
            get_results=True)
    
def get_team_matches_summary(team_name: str):
    with conn:
        return conn.select_as_dict(f"SELECT * FROM TeamAppearancesResultsSummary('{team_name}')")