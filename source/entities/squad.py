from dataclasses import dataclass 

@dataclass
class Squad:
	
    player_id: str
    player_name: str
    team_id: str
    position: str
    shirt_number: int
    home_team: bool