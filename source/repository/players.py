from entities.player import Player
from db.DbConnection import conn, StoredProcedure
from .utils import to_dataframe
from .entity import EntityRepository



class PlayerRepository(EntityRepository):

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


class PlayerStatisticsRepository(EntityRepository):

    def get_minutes_played(self, player_id: str):
        return StoredProcedure("MinutesPlayedAndBenched", playerid=player_id).call(self.conn)[0]
        
    @to_dataframe
    def get_number_of_games_as_starter(self, player_id) -> dict[str, list[str | int]]:
        data = StoredProcedure("GamesAsStarterOrSubstitute", playerid=player_id).call(self.conn)[0]
        return {
            "starter_or_sub": ["starter", "substitute"],
            "number_of_matches": [data.starter, data.substitute]
        }


player_repository = PlayerRepository(conn)
player_stats_repository = PlayerStatisticsRepository(conn)