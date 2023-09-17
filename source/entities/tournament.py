from dataclasses import dataclass
from datetime import datetime


@dataclass 
class Tournament:

    tournament_id: str
    tournament_name: str
    year: str
    start_date: datetime
    end_date: datetime
    host_country: str


@dataclass
class TournamentSummary:

    tournament_id: str
    tournament_name: str
    number_of_matches: int
    number_of_goals: int
    yellow_cards: int
    red_cards: int