from flask import Blueprint, render_template, request
from repository.tournaments import tournament_repository, tournament_stats_repository
import Visualizations.plots as vis

tournaments = Blueprint('tournaments', __name__)

def generate_data(tournament_id: str):
    return {
        "tournament": tournament_repository.get_by_id(tournament_id),
        "tournaments_list": tournament_repository.get_all(),
        "most_goals_in_single_game": tournament_stats_repository.get_most_goals_in_single_game(tournament_id),
        "most_cards_in_single_game": tournament_stats_repository.get_most_cards_in_single_game(tournament_id),
        "top_scorers": tournament_stats_repository.get_top_scorers(tournament_id=tournament_id, how_many=10)
    }

def generate_visualizations(tournament_id: str):
    return {
        "goals_by_minutes": vis.goals_by_minutes(tournament_stats_repository.get_goals_by_minutes(tournament_id)),
        "goals_difference": vis.goals_difference_by_team(tournament_stats_repository.get_goals_difference_by_team(tournament_id))
    }


@tournaments.route("/tournaments")
def tournament_details():
    tournament_id = request.args.get('id', default=None)
    data = generate_data(tournament_id)
    visualizations = generate_visualizations(tournament_id)
    return render_template("tournaments.html", data=data, visualizations=visualizations)