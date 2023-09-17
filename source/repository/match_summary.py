from entities.match import MatchSummary
from .entity import EntityRepository
from Db.DbConnection import conn, StoredProcedure


class MatchSummaryRepository(EntityRepository):

    def get_by_id(self, match_id: str) -> MatchSummary:
        return MatchSummary(*StoredProcedure("MatchResult", matchid=match_id).call(self.conn)[0])
    
    def get_by_tournament(self, tournament_id: str) -> list[MatchSummary]:
        records = StoredProcedure("MatchesResultsByTournament", tournamentid=tournament_id).call(self.conn)
        return [MatchSummary(*record) for record in records]
    
    def get_by_player(self, player_id: str) -> list[MatchSummary]:
        records = StoredProcedure("PlayerMatches", playerid=player_id).call(self.conn)
        return [MatchSummary(*record) for record in records]

    def get_by_team(self, team_id: str) -> list[MatchSummary]:
        records = StoredProcedure("TeamMatches", teamid=team_id).call(self.conn)
        return [MatchSummary(*record) for record in records]

    def get_biggest_win_of_team(self, team_id: str) -> MatchSummary | None:
        try:
            data = StoredProcedure("BiggestWin", teamid=team_id).call(conn)[0]
            return MatchSummary(*data)
        except IndexError:
            return None

    def get_biggest_defeat_of_team(self, team_id: str) -> MatchSummary:
        data = StoredProcedure("BiggestDefeat", teamid=team_id).call(conn)[0]
        return MatchSummary(*data)
    
    def get_most_goals_in_single_game(self, tournament_id: str=None) -> MatchSummary:
        data =  StoredProcedure("MostGoalsInSingleGame", tournamentid=tournament_id).call(self.conn)[0]
        return MatchSummary(*data)

    def get_most_cards_in_single_game(self, tournament_id: str=None, how_many: int=1) -> MatchSummary | None:
        try:
            data = StoredProcedure("MostBookingsByGames", tournamentid=tournament_id, how_many=how_many).call(self.conn)[0]
            return MatchSummary(*data)
        except IndexError:
            return None
        

match_summary_repository = MatchSummaryRepository(conn)