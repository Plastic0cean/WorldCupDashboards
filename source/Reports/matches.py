from Db.DbConnection import conn, DBConnection
from Db.DbTableFunction import DbTableFunction


class MatchRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_by_id(self, match_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM [matches] WHERE [match_id] = '{match_id}' ORDER BY [match_date]", True)

    def get_list_of_matches_by_tournament(self, tournament_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM [matches] WHERE [tournament_id] = '{tournament_id}' ORDER BY [match_date]", True)
        
    def get_matches_by_player(self, player_id: str):
        with self.conn:
            return DbTableFunction("PlayerMatches", parameters=player_id).select(self.conn, sort_by="match_date")
        
    def get_events(self, match_id: str):
        with self.conn:
            return DbTableFunction("MatchEvents", parameters=match_id).select(self.conn, sort_by="minute, team_id")

    def get_bookings_of_match(self, match_id: str):
            with self.conn:
                return self.conn.execute(f"SELECT * FROM bookings WHERE [match_id] = '{match_id}'", True)
            
    def get_substitutions_of_match(self, match_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM substitutions WHERE [match_id] = '{match_id}'", True)


repository = MatchRepository(conn)