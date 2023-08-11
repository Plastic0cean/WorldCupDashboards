from Db.DbConnection import conn, DBConnection, StoredProcedure
from .utils import to_dataframe


class TournamentRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_all(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM tournaments")

    def get_by_id(self, tournament_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM tournaments WHERE tournament_id = '{tournament_id}'")


class TournamentStatisticsRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_top_scorers(self, tournament_id: str=None, how_many: int=None):
        return StoredProcedure("TopScorersOfTournament", tournamentid=tournament_id, how_many=how_many).call(self.conn)

    def get_most_goals_in_single_game(self, tournament_id: str=None):
        return StoredProcedure("MostGoalsInSingleGame", tournamentid=tournament_id).call(self.conn)

    def get_most_cards_in_single_game(self, tournament_id: str=None, how_many: int=1):
        try:
            return StoredProcedure("MostBookingsByGames", tournamentid=tournament_id, how_many=how_many).call(self.conn)[0]
        except IndexError:
            return

    @to_dataframe
    def get_goals_by_minutes(self, tournament_id: str=None):
        return StoredProcedure("GoalsByMinutes", tournamentid=tournament_id).to_dict(self.conn)

    @to_dataframe
    def get_goals_difference_by_team(self, tournament_id: str=None):
        return StoredProcedure("GoalsDifferenceByTeam", tournamentid=tournament_id).to_dict(self.conn)
        

tournament_repository = TournamentRepository(conn)
tournament_stats_repository = TournamentStatisticsRepository(conn)