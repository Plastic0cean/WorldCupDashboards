from dataclasses import dataclass

@dataclass
class TopScorer:

    player_id: str
    player_name: str
    team_id: str
    team_name: str
    goals: int