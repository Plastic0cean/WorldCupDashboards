from Db.DbConnection import conn, DBConnection
from Db.DbTableFunction import DbTableFunction
from .utils import to_dataframe

class TeamRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn
    
    def get_all(self) -> list:
        with self.conn:
            names = self.conn.execute("SELECT team_id, team_name FROM Teams", True)
        return [name for name in names]

    def get_by_id(self, team_id: str):
        with self.conn:
            return self.conn.execute(f"SELECT * FROM teams WHERE team_id='{team_id}'", True)[0]

    def get_biggest_win(self, team_id: str):
        return DbTableFunction("BiggestWinOfTeam", team_id).select(self.conn)

    def get_biggest_defeat(self, team_id: str):
        return DbTableFunction("BiggestDefeatOfTeam", team_id).select(self.conn)

    def get_top_scorers(self, team_id: str, how_many: int=None):
        top = ""
        if how_many:
            top = f"TOP {how_many}"
        with self.conn:
            return self.conn.execute(
                f"SELECT {top} * FROM TeamScorers ('{team_id}') ORDER BY goals_number DESC", 
                get_results=True)

    def get_position_by_tournaments(self, team_id: str):
        return DbTableFunction("TeamPositionOnTournaments", team_id).select(self.conn, sort_by="tournament_name")

    @to_dataframe
    def get_minutes_played_by_players(self, team_id: str):
        return DbTableFunction("MinutesPlayedByTeamPlayers", team_id).select_as_dict(self.conn, sort_by="minutes_played", descending=True, limit=20)

    @to_dataframe
    def get_goals_by_opponent(self, team_id: str):
        return DbTableFunction("GoalsByOpponent", team_id).select_as_dict(self.conn)

    @to_dataframe
    def get_goals_by_tournament(self, team_id: str):
        return DbTableFunction("GoalsByTournament", team_id).select_as_dict(self.conn)
        
    @to_dataframe
    def get_list_of_matches(self, team_id: str):
        return DbTableFunction("AllMatchesByTeam", team_id).select_as_dict(self.conn)

    @to_dataframe
    def get_matches_results(self, team_id: str):
        with self.conn:
            return self.conn.select_as_dict(f"SELECT * FROM TeamAppearancesResultsSummary('{team_id}')")
        
    def get_goals_and_matches_summary(self, team_id: str):
        return DbTableFunction("GoalsAndMatchesSummary", team_id).select(self.conn)[0]
    
    
repository = TeamRepository(conn)