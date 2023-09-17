from dataclasses import dataclass

@dataclass
class Player:

    id: str
    given_name: str
    family_name: str
    birth_date: str
    team_ids: list[str]
    nationalities: list[str]
    positions: list[str]

    @property
    def name(self) -> str:
        return f"{self.given_name} {self.family_name}" if self.given_name else self.family_name
    
    @property
    def positions_str(self, sep: str="/") -> str:
        return sep.join(self.positions)
    
    def get_teams(self):
        return [(team_id, nationality) for team_id, nationality in zip(self.team_ids, self.nationalities)]
