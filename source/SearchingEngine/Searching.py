from .FuzzyStringsMatcher import FuzzyStringsMatcher

matcher = FuzzyStringsMatcher(0.8)

def fuzzy_filter_players(players_list: list, searched_string: str) -> list:
    result = []
    for player in players_list:
        if matcher.contains_substring(player.Name, searched_string):
            result.append(player)
    return result
        
