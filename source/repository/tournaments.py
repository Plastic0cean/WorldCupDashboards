from db.DbConnection import conn, StoredProcedure
from .utils import to_dataframe
from entities.tournament import Tournament, TournamentSummary
from .entity import EntityRepository


class TournamentRepository(EntityRepository):

    def get_all(self) -> list[Tournament]:
        with self.conn:
            tournaments =  self.conn.execute("SELECT * FROM tournaments")
        return [Tournament(*tournament) for tournament in tournaments]

    def get_by_id(self, tournament_id: str) -> Tournament | None:
        with self.conn:
            tournament = self.conn.execute(f"SELECT * FROM tournaments WHERE tournament_id = '{tournament_id}'")
        return None if len(tournament)==0 else Tournament(*tournament[0])


class TournamentSummaryRepository(EntityRepository):

    def get_by_player(self, player_id: str) -> list[TournamentSummary]:
        records = StoredProcedure("PlayerTournamentSummary", playerid=player_id).call(self.conn)
        return [TournamentSummary(*record) for record in records]


class TournamentStatisticsRepository(EntityRepository):

    @to_dataframe
    def get_goals_by_minutes(self, tournament_id: str=None):
        return StoredProcedure("GoalsByMinutes", tournamentid=tournament_id).to_dict(self.conn)

    @to_dataframe
    def get_goals_difference_by_team(self, tournament_id: str=None):
        return StoredProcedure("GoalsDifferenceByTeam", tournamentid=tournament_id).to_dict(self.conn)
        

tournament_repository = TournamentRepository(conn)
tournament_stats_repository = TournamentStatisticsRepository(conn)
tournament_summary_repository = TournamentSummaryRepository(conn)