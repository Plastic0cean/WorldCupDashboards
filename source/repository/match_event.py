from entities.match_event import MatchEvent 
from .entity import EntityRepository
from Db.DbConnection import conn, StoredProcedure


class MatchEventRepository(EntityRepository):

    def get_by_match(self, match_id: str) -> list[MatchEvent]:
        events = StoredProcedure("MatchEvents", matchid=match_id).call(self.conn)
        return [MatchEvent(*event) for event in events]


events_repository = MatchEventRepository(conn)