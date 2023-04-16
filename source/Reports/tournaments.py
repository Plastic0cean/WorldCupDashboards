from Db.DbConnection import conn

def get_tournaments_list():
    with conn:
        return conn.execute("SELECT * FROM TournamentList()", True)

def get_goals_and_games_by_tournament():
    with conn:
        return conn.select_as_dict("SELECT * FROM GoalsAndMatchesByTournament()")


def get_top_scorers(tournament_id: str=None, how_many: int=None):
    if tournament_id:
        tournament_id = "'" + tournament_id + "'"
    else:
        tournament_id="NULL"
    top = f"TOP {how_many} " if how_many else ""
    query = f"SELECT {top} * FROM TopScorersOfTournament({tournament_id}) ORDER BY goals DESC"
    with conn:
        return conn.execute(query, True)
    

def get_most_goals_in_single_game(tournament_id: str=None):
    if tournament_id:
        tournament_id = "'" + tournament_id + "'"
    else:
        tournament_id="NULL"
    query = f"SELECT * FROM MostGoalsInSingleGame({tournament_id})"
    with conn:
        return conn.execute(query, True)


def get_most_cards_in_single_game(tournament_id: str=None):
    if tournament_id:
        tournament_id = "'" + tournament_id + "'"
    else:
        tournament_id="NULL"
    query = f"SELECT * FROM MostBookingsByGames({tournament_id})"
    with conn:
        return conn.execute(query, True)

def get_number_of_matches_on_stadiums(tournament_id: str=None):
    if tournament_id:
        tournament_id = "'" + tournament_id + "'"
    else:
        tournament_id="NULL"
    query = f"SELECT * FROM NumberOfMatchesByStadiums({tournament_id})"
    with conn:
        return conn.select_as_dict(query)



def get_wins_ranking():
    pass