from Db.DbConnection import conn, DBConnection
from Db.DbTableFunction import DbTableFunction
from .utils import to_dataframe


class PlayerRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn
    
    def get_all(self):
        return DbTableFunction("PlayersList").select(self.conn, sort_by="name")
    
    def get_by_id(self, player_id: str):
        return DbTableFunction("GetPlayerById", player_id).select(self.conn)[0]

    @to_dataframe
    def get_goals_by_team(self, player_id: str):
        return DbTableFunction("PlayerGoalsByTeam", player_id).select_as_dict(self.conn, sort_by="number_of_goals")
    
    def get_awards(self, player_id: str):
        return DbTableFunction("PlayerAwards", player_id).select(self.conn)
    
    def get_apperances_summary(self, player_id: str):
        return DbTableFunction("PlayerTournamentSummary", player_id).select(self.conn)

    def get_positions(self, player_id: str):
        with self.conn:
            positions = self.conn.execute(f"SELECT DISTINCT position_name FROM player_appearances WHERE player_id = '{player_id}'", True)
            return [position[0] for position in positions]

    def get_minutes_played(self, player_id: str):
        with self.conn:
            query = f"""
            SELECT 
            SUM(minutes_played) AS minutes_played,
            SUM(possible_minutes - minutes_played) AS minutes_on_bench
            FROM PlayerMinutesPlayedByMatches('{player_id}')
            """
            return self.conn.select_as_dict(query)

    @to_dataframe
    def get_number_of_games_as_starter(self, player_id):
        with self.conn:
            query = f"""
                SELECT 
                    SUM(CAST(starter AS INT)) AS starter,
                    SUM(CAST(substitute AS INT)) AS substitute
                FROM player_appearances 
            WHERE player_id = '{player_id}'
            """
            result = self.conn.execute(query, True)
        
        return {
            "starer_or_sub": ["starter", "substitute"],
            "number_of_matches": [result[0].starter, result[0].substitute]
        }


repository = PlayerRepository(conn)