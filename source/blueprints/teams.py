import os
from flask import Blueprint, render_template, send_from_directory
from entities.match import MatchesSummaryCollection
from repository.teams import team_repository, team_stats_repository
from repository.match_summary import match_summary_repository
from repository.top_scorers import top_scorers_repository
import visualizations.plots as plt


teams = Blueprint('teams', __name__)


def generate_data(team_id: str):
    return {
        "team": team_repository.get_by_id(team_id),
        "biggest_win": match_summary_repository.get_biggest_win_of_team(team_id),
        "biggest_defeat": match_summary_repository.get_biggest_defeat_of_team(team_id),
        "top_scorers": top_scorers_repository.get_by_team(team_id, 10),
        "position_by_tournament": team_stats_repository.get_position_by_tournaments(team_id),
        "matches": MatchesSummaryCollection(match_summary_repository.get_by_team(team_id)).to_dict("tournament_id")
    }

def generate_visualizations(team_id):
    return {
        "matches_results": plt.results_of_matches(team_stats_repository.get_results_summary(team_id)),
        "goals_by_opponent": plt.team_goals_by_opponent(team_stats_repository.get_goals_by_opponent(team_id)),
        "goals_by_tournament": plt.team_goals_by_tournament(team_stats_repository.get_goals_by_tournament(team_id)),
        "most_minutes_by_player": plt.players_with_most_minutes(team_stats_repository.get_minutes_played_by_players(team_id)),
        "matches_chart": plt.all_matches_by_team(team_stats_repository.get_list_of_matches(team_id))
    }


@teams.route("/teams/<team_id>", methods=("GET", "POST"))
def team_details(team_id: str):
    data = generate_data(team_id)
    visualizations = generate_visualizations(team_id)
    return render_template("team_details.html", data=data, visualizations=visualizations)


@teams.route("/teams", methods=("GET", "POST"))
def teams_selection():
    teams = team_repository.get_all()
    return render_template("team_selection.html", teams=teams)


@teams.route("/flags/<team_id>")
def flag(team_id: str):
    return send_from_directory(os.path.join("static", "images", "flags"), team_id + ".jpg")