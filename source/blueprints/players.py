from flask import Blueprint, render_template, request
from entities.match import MatchesSummaryCollection
from repository.players import player_repository, player_stats_repository
from repository.awards import awards_repository
from repository.tournaments import tournnamet_summary_repository
from repository.match_summary import match_summary_repository
from SearchingEngine.Searching import players_searching
import visualizations.plots as plt

players = Blueprint("players", __name__)

def generate_data(player_id):
    return {
        "appearances_summary": tournnamet_summary_repository.get_by_player(player_id),
        "matches": MatchesSummaryCollection(match_summary_repository.get_by_player(player_id)).to_dict("tournament_id"),
        "awards": awards_repository.get_player_awards(player_id),
        "player": player_repository.get_by_id(player_id),
        "positions": player_repository.get_positions(player_id)
    }


def generate_visualizations(player_id):
    return {
        "minutes_played": plt.overall_minutes_played(player_stats_repository.get_minutes_played(player_id)),
        "starter_or_sub": plt.starter_or_substitute(player_stats_repository.get_number_of_games_as_starter(player_id))
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