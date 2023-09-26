from searching.PlayerSearching import PlayersSeaching
from searching.FuzzyStringsMatcher import FuzzyStringsMatcher
from entities.player import Player
import pytest

@pytest.fixture
def players():
    players = [
        Player("id1", "Robert", "Lewandowski", "1900-01-01", "team1", ["PL"], ["FW"]),
        Player("id1", "Don", "Joe", "1900-01-01", "team1", ["PL"], ["FW"])
        ]
    return players

@pytest.fixture
def player_searching_ignore_cases():
    engine = FuzzyStringsMatcher(0.8, True)
    return PlayersSeaching(engine)

@pytest.fixture
def player_searching_not_ignore_cases():
    engine_not_ignore = FuzzyStringsMatcher(0.9, False)
    return PlayersSeaching(engine_not_ignore)


def test_search_ignore_cases(player_searching_ignore_cases, players):
    result = player_searching_ignore_cases.search(players, "LEWANDOWSKY")
    assert result[0].family_name == "Lewandowski"
    assert len(result)==1

def test_search_not_ignore_cases_not_found(player_searching_not_ignore_cases, players):
    result = player_searching_not_ignore_cases.search(players, "LEWANDOWSKY")
    assert result == []




