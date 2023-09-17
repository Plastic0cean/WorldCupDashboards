from entities.top_scorer import TopScorer
from .entity import EntityRepository
from Db.DbConnection import conn, StoredProcedure


class TopScorersRepository(EntityRepository):

    def get_by_tournament(self, tournament_id: str=None, how_many: int=None):
        records = StoredProcedure("TopScorersOfTournament", tournamentid=tournament_id, how_many=how_many).call(self.conn)
        return [TopScorer(*record) for record in records]
    
    def get_by_team(self, team_id: str, how_many: int=None):
        records = StoredProcedure("TopScorersOfTeam", teamid=team_id, how_many=how_many).call(conn)
        return [TopScorer(*record) for record in records]


top_scorers_repository = TopScorersRepository(conn)