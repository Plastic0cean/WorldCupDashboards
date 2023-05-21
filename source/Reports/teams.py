from Db.DbConnection import conn
from Db.DbTableFunction import DbTableFunction

def get_all_team_names():
    with conn:
        names = conn.execute("SELECT team_id, team_name FROM Teams", True)
    return [name for name in names]

def get_team_by_id(team_id: str):
    with conn:
        return conn.execute(f"SELECT * FROM teams WHERE team_id='{team_id}'", True)[0]

def get_goal_ranking_by_team(team_id: str):
    with conn: 
        query = f"SELECT * FROM vGoalsRankingByTeam WHERE team_id = '{team_id}'"
        result = conn.execute(query, get_results=True)
    if result:
        return result[0]

def get_biggest_win(team_id: str):
    return DbTableFunction("BiggestWinOfTeam", team_id).select(conn)

def get_biggest_defeat(team_id: str):
    return DbTableFunction("BiggestDefeatOfTeam", team_id).select(conn)

def get_top_scorers(team_id: str, how_many: int=None):
    top = ""
    if how_many:
        top = f"TOP {how_many}"
    with conn:
        return conn.execute(
            f"SELECT {top} * FROM TeamScorers ('{team_id}') ORDER BY goals_number DESC", 
            get_results=True)

def get_position_by_tournaments(team_id: str):
    return DbTableFunction("TeamPositionOnTournaments", team_id).select(conn, sort_by="tournament_name")

def get_minutes_played_by_players(team_id: str):
    return DbTableFunction("MinutesPlayedByTeamPLayers", team_id).select_as_dict(conn, sort_by="minutes_played", descending=True, limit=20)

def get_goals_by_opponent(team_id: str):
    return DbTableFunction("GoalsByOpponent", team_id).select_as_dict(conn)

def get_goals_by_tournament(team_id: str):
    return DbTableFunction("GoalsByTournament", team_id).select_as_dict(conn)
    
def get_list_of_matches(team_id: str):
    return DbTableFunction("AllMatchesByTeam", team_id).select_as_dict(conn)

def get_matches_results(team_id: str):
    with conn:
        return conn.select_as_dict(f"SELECT * FROM TeamAppearancesResultsSummary('{team_id}')")
    
def get_goals_and_matches_summary(team_id: str):
    return DbTableFunction("GoalsAndMatchesSummary", team_id).select(conn)[0]