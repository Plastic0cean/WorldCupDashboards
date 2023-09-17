from dataclasses import dataclass


class TournamentSummary:

    tournament_id: str
    tournament_name: str
    number_of_matches: int
    goals: int
    yellow_cards: int
    red_cards: int