from db.DbConnection import conn, DBConnection, StoredProcedure


class SquadsRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_team_squad_by_match(self, match_id: str, home_team: bool):
        return StoredProcedure("SquadsByMatch", matchid=match_id, hometeam=home_team).call(self.conn)
    

squads_repository = SquadsRepository(conn)