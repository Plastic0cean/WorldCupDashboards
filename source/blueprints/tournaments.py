from flask import Blueprint, render_template, request
from Reports.tournaments import repository
import Visualizations.plots as vis

tournaments = Blueprint('tournaments', __name__)

def generate_data(tournament_id: str, repository):
    return {
        "tournament": repository.get_by_id(tournament_id),
        "tournaments_list": repository.get_all(),
        "most_goals_in_single_game": repository.get_most_goals_in_single_game(tournament_id),
        "most_cards_in_single_game": repository.get_most_cards_in_single_game(tournament_id),
        "top_scorers": repository.get_top_scorers(tournament_id=tournament_id, how_many=10)
    }

def generate_visualizations(tournament_id: str, repository):
    return {
        "goals_by_tournament": vis.goals_by_tournament(repository.get_goals_and_games_by_tournament()),
        "goals_by_minutes": vis.goals_by_minutes(repository.get_goals_by_minutes(tournament_id)),
        "goals_difference": vis.goals_difference_by_team(repository.get_goals_difference_by_team(tournament_id))
    }


@tournaments.route("/tournaments")
def tournament_details():
    tournament_id = request.args.get('id', default=None)
    data = generate_data(tournament_id, repository)
    visualizations = generate_visualizations(tournament_id, repository)
    return render_template("tournaments.html", data=data, visualizations=visualizations)