import os
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from Reports.teams import repository
from utils.utils import retry_if_fail
import Visualizations.plots as vis

teams = Blueprint('teams', __name__)

def generate_data(team_id: str, repository):
    return {
        "team": repository.get_by_id(team_id),
        "goals_and_matches": repository.get_goals_and_matches_summary(team_id),
        "biggest_win": repository.get_biggest_win(team_id),
        "biggest_defeat": repository.get_biggest_defeat(team_id),
        "top_scorers": repository.get_top_scorers(team_id, 10),
        "position_by_tournament": repository.get_position_by_tournaments(team_id)
    }

def generate_visualizations(team_id, repository):
    return {
        "matches_results": vis.results_of_matches_pie(repository.get_matches_results(team_id)),
        "goals_by_opponent": vis.team_goals_by_opponent(repository.get_goals_by_opponent(team_id)),
        "goals_by_tournament": vis.team_goals_by_tournament(repository.get_goals_by_tournament(team_id)),
        "most_minutes_by_player": vis.players_with_most_minutes(repository.get_minutes_played_by_players(team_id)),
        "matches_chart": vis.all_matches_by_team(repository.get_list_of_matches(team_id))
    }

@teams.route("/teams/<team_id>", methods=("GET", "POST"))
def team_details(team_id: str):
    data = generate_data(team_id, repository)
    visualizations = generate_visualizations(team_id, repository)
    return render_template("team_detals.html", data=data, visualizations=visualizations)

@teams.route("/teams", methods=("GET", "POST"))
def teams_selection():
    teams = repository.get_all()
    if request.method == "POST":
        team_id = request.form["teams-dropdown"]
        return redirect(url_for("teams.team_details", team_id=team_id))
    return render_template("team_selection.html", teams=teams)

@retry_if_fail
def get_flag_filename(team_id: str):
    filename = repository.get_by_id(team_id).flag_img
    return filename

@teams.route("/flags/<team_id>")
def display_flag(team_id: str):
    filename = get_flag_filename(team_id)
    return send_from_directory(os.path.join("static", "images", "flags"), filename)