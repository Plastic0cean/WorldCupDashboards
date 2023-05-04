from Db.DbConnection import conn
from Db.DbTableFunction import DbTableFunction

def get_tournaments_list():
    return DbTableFunction("TournamentList").select(conn)

def get_goals_and_games_by_tournament():
    return DbTableFunction("GoalsAndMatchesByTournament").select_as_dict(conn)

def get_top_scorers(tournament_id: str=None, how_many: int=None):
    return DbTableFunction("TopScorersOfTournament", tournament_id, use_default_parameters=True).select(conn, sort_by="goals", descending=True, limit=how_many)
    
def get_most_goals_in_single_game(tournament_id: str=None):
    return DbTableFunction("MostGoalsInSingleGame", tournament_id, use_default_parameters=True).select(conn)

def get_most_cards_in_single_game(tournament_id: str=None):
    return DbTableFunction("MostBookingsByGames", tournament_id, use_default_parameters=True).select(conn)

def get_number_of_matches_on_stadiums(tournament_id: str=None):
    return DbTableFunction("NumberOfMatchesByStadiums", tournament_id, use_default_parameters=True).select_as_dict(conn)

def get_wins_ranking():
    pass