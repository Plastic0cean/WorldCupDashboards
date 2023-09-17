from Db.DbConnection import conn, DBConnection, StoredProcedure
from .utils import to_dataframe


class TeamRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn
    
    def get_all(self) -> list:
        with self.conn:
            names = self.conn.execute("SELECT * FROM teams")
        return [name for name in names]

    def get_by_id(self, team_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM teams WHERE team_id='{team_id}'")[0]

        
class TeamStatisticsRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_position_by_tournaments(self, team_id: str):
        return StoredProcedure("PositionsOnTournaments", teamid=team_id).call(conn)

    @to_dataframe
    def get_minutes_played_by_players(self, team_id: str, how_many: int=20):
        return StoredProcedure("MinutesPlayedByPlayers", teamid=team_id, how_many=how_many).to_dict(conn)

    @to_dataframe
    def get_goals_by_opponent(self, team_id: str):
        return StoredProcedure("GoalsByOpponent", teamid=team_id).to_dict(conn)

    @to_dataframe
    def get_goals_by_tournament(self, team_id: str):    
        return StoredProcedure("GoalsByTournament", teamid=team_id).to_dict(conn)
        
    @to_dataframe
    def get_list_of_matches(self, team_id: str):
        return StoredProcedure("MatchesOfTeam", teamid=team_id).to_dict(conn) #TODO: Move to matches repository

    @to_dataframe
    def get_results_summary(self, team_id: str):
        data = StoredProcedure("ResultsSummary", teamid=team_id).call(conn)[0]
        return {
            "result": ["wins", "loses", "draws"],
            "number": [data.wins, data.loses, data.draws]
            }
        
    
team_repository = TeamRepository(conn)
team_stats_repository = TeamStatisticsRepository(conn)