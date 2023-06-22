from Db.DbConnection import conn, DBConnection
from Db.DbTableFunction import DbTableFunction
from .utils import to_dataframe


class TournamentRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_all(self):
        return DbTableFunction("TournamentList").select(self.conn)

    def get_by_id(self, tournament_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM tournaments WHERE tournament_id = '{tournament_id}'", True)

    def get_goals_and_games_by_tournament(self):
        return DbTableFunction("GoalsAndMatchesByTournament").select_as_dict(self.conn)

    def get_top_scorers(self, tournament_id: str=None, how_many: int=None):
        return DbTableFunction("TopScorersOfTournament", tournament_id, use_default_parameters=True).select(self.conn, sort_by="goals", descending=True, limit=how_many)
        
    def get_most_goals_in_single_game(self, tournament_id: str=None):
        return DbTableFunction("MostGoalsInSingleGame", tournament_id, use_default_parameters=True).select(self.conn)[0]

    def get_most_cards_in_single_game(self, tournament_id: str=None):
        try:
            return DbTableFunction("MostBookingsByGames", tournament_id, use_default_parameters=True).select(self.conn)[0]
        except IndexError:
            return

    @to_dataframe
    def get_goals_by_minutes(self, tournament_id: str=None):
        return DbTableFunction("GoalsByMinutes", tournament_id, use_default_parameters=True).select_as_dict(self.conn)

    @to_dataframe
    def get_goals_difference_by_team(self, tournament_id: str=None):
        return DbTableFunction("GoalsDifferenceByTeam", tournament_id, use_default_parameters=True).select_as_dict(self.conn)
        

repository = TournamentRepository(conn)