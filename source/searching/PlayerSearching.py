from .FuzzyStringsMatcher import FuzzyStringsMatcher
from Config import config


class PlayersSeaching:

    def __init__(self, engine) -> None:
        self.engine = engine

    def search(self, players_list: list, searched_string: str) -> list:
        result = []
        for player in players_list:
            if engine.contains_substring(player.given_name, searched_string) or engine.contains_substring(player.family_name, searched_string):
                result.append(player)
        return result
        

engine = FuzzyStringsMatcher(config.searching_threshold)
players_searching = PlayersSeaching(engine)