from Db.DbConnection import conn
from Db.DbTableFunction import DbTableFunction
from .utils import to_dataframe

def get_tournaments_list():
    return DbTableFunction("TournamentList").select(conn)

def get_tournament_by_id(tournament_id: str):
    with conn:
       return conn.execute(f"SELECT * FROM tournaments WHERE tournament_id = '{tournament_id}'", True)

def get_goals_and_games_by_tournament():
    return DbTableFunction("GoalsAndMatchesByTournament").select_as_dict(conn)

def get_top_scorers(tournament_id: str=None, how_many: int=None):
    return DbTableFunction("TopScorersOfTournament", tournament_id, use_default_parameters=True).select(conn, sort_by="goals", descending=True, limit=how_many)
    
def get_most_goals_in_single_game(tournament_id: str=None):
    return DbTableFunction("MostGoalsInSingleGame", tournament_id, use_default_parameters=True).select(conn)[0]

def get_most_cards_in_single_game(tournament_id: str=None):
    try:
        return DbTableFunction("MostBookingsByGames", tournament_id, use_default_parameters=True).select(conn)[0]
    except IndexError:
        return


def get_number_of_matches_on_stadiums(tournament_id: str=None):
    return DbTableFunction("NumberOfMatchesByStadiums", tournament_id, use_default_parameters=True).select_as_dict(conn)

@to_dataframe
def get_goals_by_minutes(tournament_id: str=None):
    return DbTableFunction("GoalsByMinutes", tournament_id, use_default_parameters=True).select_as_dict(conn)

@to_dataframe
def get_goals_difference_by_team(tournament_id: str=None):
    return DbTableFunction("GoalsDifferenceByTeam", tournament_id, use_default_parameters=True).select_as_dict(conn)
    
def get_power_ranking(tournament_id: str=None):
    return DbTableFunction("TeamsPowerRanking", tournament_id, use_default_parameters=True).select(conn, sort_by="points", descending=True)