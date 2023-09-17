from collections import defaultdict
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


class EventsCollection:
    # TODO: Check if it's used anywhere

    def __init__(self, events: list[MatchEvent]=None) -> None:
        if events:
            self.events = events
        else:
            self.events = []

    def add(self, event: MatchEvent) -> None:
        self.events.append(event)

    def to_dict(self):
        def default_value():
            return {"home_team": [], "away_team": []}
        result_events = defaultdict(default_value)
        for event in self.events:
            if event.home_team == 1:
                result_events[event.minute_label]["home_team"].append(event)
            else:
                result_events[event.minute_label]["away_team"].append(event)
        return dict(result_events)