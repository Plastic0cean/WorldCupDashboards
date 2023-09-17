from Db.DbConnection import conn, DBConnection, StoredProcedure
from .utils import to_dataframe
from .entity import EntityRepository


class TournamentRepository(EntityRepository):

    def get_all(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM tournaments")

    def get_by_id(self, tournament_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM tournaments WHERE tournament_id = '{tournament_id}'")


class TournamentSummaryRepository(EntityRepository):

    def get_by_player(self, player_id: str):
        return StoredProcedure("PlayerTournamentSummary", playerid=player_id).call(self.conn)


class TournamentStatisticsRepository(EntityRepository):

    @to_dataframe
    def get_goals_by_minutes(self, tournament_id: str=None):
        return StoredProcedure("GoalsByMinutes", tournamentid=tournament_id).to_dict(self.conn)

    @to_dataframe
    def get_goals_difference_by_team(self, tournament_id: str=None):
        return StoredProcedure("GoalsDifferenceByTeam", tournamentid=tournament_id).to_dict(self.conn)
        

tournament_repository = TournamentRepository(conn)
tournament_stats_repository = TournamentStatisticsRepository(conn)
tournnamet_summary_repository = TournamentSummaryRepository(conn)