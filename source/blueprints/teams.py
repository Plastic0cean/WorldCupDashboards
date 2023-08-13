import os
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from repository.teams import team_repository, team_stats_repository
from repository.matches import match_repository
from utils.utils import retry_if_fail
import Visualizations.plots as vis

teams = Blueprint('teams', __name__)

def generate_data(team_id: str):
    return {
        "team": team_repository.get_by_id(team_id),
        "biggest_win": team_stats_repository.get_biggest_win(team_id),
        "biggest_defeat": team_stats_repository.get_biggest_defeat(team_id),
        "top_scorers": team_stats_repository.get_top_scorers(team_id, 10),
        "position_by_tournament": team_stats_repository.get_position_by_tournaments(team_id),
        "matches": match_repository.get_matches_by_team(team_id).to_dict()
    }

def generate_visualizations(team_id):
    return {
        "matches_results": vis.results_of_matches(team_stats_repository.get_results_summary(team_id)),
        "goals_by_opponent": vis.team_goals_by_opponent(team_stats_repository.get_goals_by_opponent(team_id)),
        "goals_by_tournament": vis.team_goals_by_tournament(team_stats_repository.get_goals_by_tournament(team_id)),
        "most_minutes_by_player": vis.players_with_most_minutes(team_stats_repository.get_minutes_played_by_players(team_id)),
        "matches_chart": vis.all_matches_by_team(team_stats_repository.get_list_of_matches(team_id))
    }

@teams.route("/teams/<team_id>", methods=("GET", "POST"))
def team_details(team_id: str):
    data = generate_data(team_id)
    visualizations = generate_visualizations(team_id)
    return render_template("team_detals.html", data=data, visualizations=visualizations)

@teams.route("/teams", methods=("GET", "POST"))
def teams_selection():
    teams = team_repository.get_all()
    if request.method == "POST":
        team_id = request.form["teams-dropdown"]
        return redirect(url_for("teams.team_details", team_id=team_id))
    return render_template("team_selection.html", teams=teams)

@retry_if_fail
def get_flag_filename(team_id: str):
    filename = team_repository.get_by_id(team_id).flag_img
    return filename

@teams.route("/flags/<team_id>")
def display_flag(team_id: str):
    filename = get_flag_filename(team_id)
    return send_from_directory(os.path.join("static", "images", "flags"), filename)