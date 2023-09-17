from entities.award import IndividualAward
from .entity import EntityRepository
from Db.DbConnection import conn, StoredProcedure


class AwardsRepository(EntityRepository):

    def get_player_awards(self, player_id: str) -> list[IndividualAward]:
        records = StoredProcedure("PlayerAwards", playerid=player_id).call(self.conn)
        return [IndividualAward(*record) for record in records]
    

awards_repository = AwardsRepository(conn)