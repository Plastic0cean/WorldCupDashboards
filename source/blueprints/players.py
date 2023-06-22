from flask import Blueprint, render_template, request
import Reports.players as repository
from SearchingEngine.Searching import players_searching
import Visualizations.plots as vis

players = Blueprint("players", __name__)

def generate_data(player_id):
    return {
        "player": repository.get_player_by_id(player_id),
        "awards": repository.get_player_awards(player_id),
        "stats": repository.get_player_basic_stats(player_id),
        "appearances_summary": repository.get_apperances_summary(player_id)
    }

def generate_visualizations(player_id):
    return {
        "goals_by_team": vis.players_goals_by_team(repository.get_player_goals_by_team(player_id)),
        "appearances_by_tournament": vis.player_appearances_by_tournament(repository.get_matches_by_tournament(player_id)),
        "minutes_played": vis.overall_minutes_played(repository.get_minutes_played(player_id)),
        "starer_or_sub": vis.starter_or_substitute(repository.get_number_of_games_as_starter(player_id))
    }

@players.route("/players", methods=("GET", "POST"))
def players_selection():
    players = repository.get_all_players_names()
    if request.method == "POST":
        players = players_searching.search(players, request.form["player"])
    return render_template("player_selection.html", players=players)

@players.route("/players/<player_id>")
def player_details(player_id: str):
    data = generate_data(player_id)
    visualizations = generate_visualizations(player_id)
    return render_template("player_details.html", data=data, visualizations=visualizations)