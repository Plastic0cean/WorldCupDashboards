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


def get_wins_ranking():
    pass