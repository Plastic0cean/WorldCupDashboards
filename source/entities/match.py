from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MatchSummary:

    tournament_id: str
    match_id: str
    home_team_id: str
    home_team_name: str
    away_team_id: str
    away_team_name: str
    score: str
    match_date: datetime
    yellow_cards: Optional[int] = None
    red_cards: Optional[int] = None


class MatchesSummaryCollection:

    def __init__(self, matches: list[MatchSummary]=None) -> None:
        if matches:
            self.matches = matches
        else:
            self.matches = []

    def add(self, match: MatchSummary) -> None:
        self.matches.append(match)

    def __to_dict_date_key(self) -> dict[datetime: list[MatchSummary]]:
        matches_dict = dict()
        for match in self.matches:
            if match.match_date in matches_dict:
                matches_dict[match.match_date].append(match)
            else:
                matches_dict[match.match_date] = [match]
        return matches_dict
    
    def __to_dict_tournament_key(self) -> dict[str: list[MatchSummary]]:
        matches_dict = dict()
        for match in self.matches:
            if match.tournament_id in matches_dict:
                matches_dict[match.tournament_id].append(match)
            else:
                matches_dict[match.tournament_id] = [match]
        return matches_dict


    def to_dict(self, key: str="match_date") -> dict[str: list[MatchSummary]]:
        if key == "match_date":
            return self.__to_dict_date_key()
        elif key == "tournament_id":
            return self.__to_dict_tournament_key()
        else:
            raise KeyError("The key can only be 'match_date' or 'tournament_id'.")