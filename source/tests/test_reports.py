"""
Please note that in order to succesfully run these tests, there should be production data stored in a database
because each of the functions runs single SQL query 
"""
import pytest
import Reports.players as player
import Reports.teams as team
import Reports.tournaments as tournament


@pytest.fixture
def test_player_id():
    return 'P-03429'

@pytest.fixture
def test_player_id2():
    return "P-08266"

@pytest.fixture
def test_team_id():
    return "T-55"

@pytest.fixture
def test_tournament_id():
    return "WC-2022"

def test_get_all_players_names():
    data = player.get_all_players_names()
    assert data[0].PlayerId == "P-00720"

def test_get_player_by_id(test_player_id):
   p = player.get_player_by_id(test_player_id)
   assert p.name == "Lionel Messi"

def test_get_player_goals_by_team(test_player_id2):
    data = player.get_player_goals_by_team(test_player_id2)
    assert data["number_of_goals"] == [1, 1]
    assert data["team"] == ["France", "Saudi Arabia"]

def test_get_player_awards(test_player_id):
    data = player.get_player_awards(test_player_id)
    assert data[0].name == "Golden Ball"
    assert data[1].name == "Golden Ball"
    assert data[2].name == "Silver Boot"

def test_get_player_basic_stats(test_player_id):
    data = player.get_player_basic_stats(test_player_id)
    assert data.goals == 13 and data.matches == 26 and data.red_cards == 0 and data.yellow_cards == 2

def test_get_apperances_summary(test_player_id):
    data = player.get_apperances_summary(test_player_id)
    assert data[0].tournament_id == 'WC-2006'
    assert data[1].tournament_id == 'WC-2010'
    assert data[2].tournament_id == 'WC-2014'
    assert data[3].tournament_id == 'WC-2018'
    assert data[4].tournament_id == 'WC-2022'

def test_get_biggest_win_by_team(test_team_id):
    data = team.get_biggest_win_by_team(test_team_id)
    assert data[0].score == "7-0"

def test_get_biggest_defeat_by_team(test_team_id):
    data = team.get_biggest_defeat_by_team(test_team_id)
    assert data[0].score == "0-4"

def test_get_top_scorers(test_team_id):
    data = team.get_top_scorers(test_team_id)
    assert data[0].player_id == "P-02554"

def test_get_team_matches_summary(test_team_id):
    data = team.get_team_matches_summary(test_team_id)
    assert data == {
        "number": [6, 15, 17],
        "result": ["draw", "lose", "win"]
    } 

def test_get_tournaments_list():
    assert tournament.get_tournaments_list()[0].tournament_id == "WC-1930"

def test_get_goals_and_games_by_tournament():
    data = tournament.get_goals_and_games_by_tournament()
    assert data["country"][0] == "Uruguay"
    assert data["matches"][0] == 18
    assert data["goals"][0] == 70

def test_get_top_scorers(test_tournament_id):
    assert tournament.get_top_scorers(test_tournament_id, how_many=1)[0].player_id == "P-06978"

def test_get_most_goals_in_single_game(test_tournament_id):
    assert tournament.get_most_goals_in_single_game(test_tournament_id)[0].number_of_goals == 8

def test_get_most_cards_in_single_game(test_tournament_id):
    assert tournament.get_most_cards_in_single_game(test_tournament_id)[0].match_id == "M-2022-58"

