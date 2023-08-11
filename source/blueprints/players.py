from flask import Blueprint, render_template, request
from repository.players import player_repository, player_stats_repository
from repository.matches import match_repository
from SearchingEngine.Searching import players_searching
import Visualizations.plots as vis

players = Blueprint("players", __name__)

def produce_matches_list(matches) -> dict:
    result = dict()
    for match in matches:
        if match.tournament_id in result:
            result[match.tournament_id].append(match)
        else:
            result[match.tournament_id] = [match]
    return result

def generate_data(player_id):
    return {
        "appearances_summary": player_stats_repository.get_apperances_summary(player_id),
        "matches": produce_matches_list(match_repository.get_matches_by_player(player_id)),
        "awards": player_stats_repository.get_awards(player_id),
        "player": player_repository.get_by_id(player_id),
        "positions": player_repository.get_positions(player_id)
    }

def generate_visualizations(player_id):
    return {
        "minutes_played": vis.overall_minutes_played(player_stats_repository.get_minutes_played(player_id)),
        "starer_or_sub": vis.starter_or_substitute(player_stats_repository.get_number_of_games_as_starter(player_id))
    }

@players.route("/players", methods=("GET", "POST"))
def players_selection():
    players = player_repository.get_all()
    if request.method == "POST":
        players = players_searching.search(players, request.form["player"])
    return render_template("player_selection.html", players=players)

@players.route("/players/<player_id>")
def player_details(player_id: str):
    data = generate_data(player_id)
    visualizations = generate_visualizations(player_id)
    return render_template("player_details.html", data=data, visualizations=visualizations)