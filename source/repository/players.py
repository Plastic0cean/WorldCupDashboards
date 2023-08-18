from Db.DbConnection import conn, DBConnection, StoredProcedure
from .utils import to_dataframe
from dataclasses import dataclass

@dataclass
class Player:

    id: str
    given_name: str
    family_name: str
    birth_date: str
    team_ids: list[str]
    nationalities: list[str]
    positions: list[str]

    @property
    def name(self) -> str:
        return f"{self.given_name} {self.family_name}" if self.given_name else self.family_name
    
    @property
    def positions_str(self, sep: str="/") -> str:
        return sep.join(self.positions)
    
    def get_teams(self):
        return [(team_id, nationality) for team_id, nationality in zip(self.team_ids, self.nationalities)]


class PlayerRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn

    def get_all(self):
        return StoredProcedure("PlayersList").call(self.conn)
    
    def get_by_id(self, player_id: str) -> Player:
        nationalities = self.get_nationalities(player_id)
        with self.conn:
            player = self.conn.execute(f"SELECT * FROM players WHERE player_id = '{player_id}'")[0]
        return Player(
            id=player.player_id,
            given_name=player.given_name,
            family_name=player.family_name,
            birth_date=player.birth_date,
            team_ids=[row.team_id for row in nationalities],
            nationalities=[row.team_name for row in nationalities],
            positions=self.get_positions(player_id)
            )
    
    def get_positions(self, player_id: str) -> list[str]:
        with self.conn:
            positions = self.conn.execute(f"SELECT DISTINCT position FROM player_appearances WHERE player_id = '{player_id}'")
            return [position[0] for position in positions]

    def get_nationalities(self, player_id: str) -> list[str]:
        with self.conn:
            nationalities = conn.execute(f"""
                SELECT DISTINCT s.team_id, t.team_name 
                FROM squads s JOIN teams t ON s.team_id = t.team_id 
                WHERE s.player_id = '{player_id}'""")
        return nationalities


class PlayerStatisticsRepository:

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn
    
    def get_awards(self, player_id: str):
        return StoredProcedure("PlayerAwards", playerid=player_id).call(self.conn)
    
    def get_apperances_summary(self, player_id: str):
        return StoredProcedure("PlayerTournamentSummary", playerid=player_id).call(self.conn)

    def get_minutes_played(self, player_id: str):
        return StoredProcedure("MinutesPlayedAndBenched", playerid=player_id).call(self.conn)[0]
        
    @to_dataframe
    def get_number_of_games_as_starter(self, player_id):
        with self.conn:
            query = f"""
                SELECT 
                    SUM(starter) AS starter,
                    SUM(substitute) AS substitute
                FROM player_appearances 
            WHERE player_id = '{player_id}'
            """
            result = self.conn.execute(query)
        
        return {
            "starer_or_sub": ["starter", "substitute"],
            "number_of_matches": [result[0].starter, result[0].substitute]
        }


player_repository = PlayerRepository(conn)
player_stats_repository = PlayerStatisticsRepository(conn)