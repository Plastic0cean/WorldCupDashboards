from dataclasses import dataclass

@dataclass
class MatchEvent: 

    match_id: str 
    player_id: str
    player_name: str
    minute_label: str
    minute: int
    team_id: str
    team_name: str
    home_team: bool
    type: str