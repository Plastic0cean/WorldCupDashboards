from Db.DbConnection import conn, StoredProcedure
# from entities.match import Matches
from .entity import EntityRepository


class MatchRepository(EntityRepository):

    def get_by_id(self, match_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM matches WHERE match_id = '{match_id}'")
                
match_repository = MatchRepository(conn)