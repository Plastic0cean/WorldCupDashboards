from dataclasses import dataclass

@dataclass
class TournamentSummary:

    tournament_id: str
    tournament_name: str
    number_of_matches: int
    number_of_goals: int
    yellow_cards: int
    red_cards: int