from Db.DbConnection import conn, DBConnection, StoredProcedure


class MatchRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_by_id(self, match_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM matches WHERE match_id = '{match_id}'")
        
    def get_result(self, match_id: str):
        return StoredProcedure("MatchResult", matchid=match_id).call(self.conn)

    def get_matches_results_by_tournament(self, tournament_id: str):
        return StoredProcedure("MatchesResultsByTournament", tournamentid=tournament_id).call(self.conn)
        
    def get_matches_by_player(self, player_id: str):
        return StoredProcedure("MatchEvents", playerid=player_id).call(self.conn)
        
    def get_events(self, match_id: str):
        return StoredProcedure("MatchEvents", matchid=match_id).call(self.conn)


match_repository = MatchRepository(conn)