from dataclasses import dataclass
from datetime import datetime
from Db.DbConnection import conn, DBConnection, StoredProcedure


@dataclass
class MatchSummary:

    tournament_id: str
    match_id: str
    home_team_id: str
    home_team_name: str
    away_team_id: str
    away_team_name: str
    score: str
    date: datetime


class Matches:

    def __init__(self, matches: list[MatchSummary]=None) -> None:
        if matches:
            self.matches = matches
        else:
            self.matches = []

    def add(self, match: MatchSummary) -> None:
        self.matches.append(match)

    def to_dict(self) -> dict[str: list]:
        matches_dict = dict()
        for match in self.matches:
            if match.tournament_id in matches_dict:
                matches_dict[match.tournament_id].append(match)
            else:
                matches_dict[match.tournament_id] = [match]
        return matches_dict
    
    @classmethod
    def from_named_object(cls, named):
        matches_list = []
        for obj in named:
            matches_list.append(MatchSummary(tournament_id=obj.tournament_id, 
                        match_id=obj.match_id, 
                        home_team_id=obj.home_team_id, 
                        home_team_name=obj.home_team_name,
                        away_team_id=obj.away_team_id, 
                        away_team_name=obj.away_team_name, 
                        score=obj.score, 
                        date=obj.match_date))
        return cls(matches_list)


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
        return StoredProcedure("PlayerMatches", playerid=player_id).call(self.conn)
    
    def get_matches_by_team(self, team_id: str):
        return Matches.from_named_object(StoredProcedure("TeamMatches", teamid=team_id).call(self.conn))
        
    def get_events(self, match_id: str):
        return StoredProcedure("MatchEvents", matchid=match_id).call(self.conn)


match_repository = MatchRepository(conn)