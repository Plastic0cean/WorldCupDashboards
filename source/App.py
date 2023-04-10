from flask import Flask, render_template, request, redirect, url_for
from Visualizations.plots import PieChartPX, render_players_goals_by_team, render_player_appearances_by_tournament, render_goals_by_tournament
import Reports.teams 
import Reports.players
import Reports.tournaments
from SearchingEngine.Searching import fuzzy_filter_players

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")


@app.route("/teams/<team_name>", methods=("GET", "POST"))
def team_details(team_name: str):
    ranking = Reports.teams.get_goal_ranking_by_team(team_name)
    win = Reports.teams.get_biggest_win_by_team(team_name)
    defeat = Reports.teams.get_biggest_defeat_by_team(team_name)
    scorers = Reports.teams.get_top_scorers(team_name, 10)
    
    results_pie_chart = PieChartPX(
        Reports.teams.get_team_matches_summary(team_name),
        ["DarkBlue", "Red", "Green"], "Overall results of games played")
    return render_template(
        "team_detals.html",
        team_name=team_name,
        ranking=ranking,
        win=win,
        defeat=defeat,
        scorers=scorers,
        results_chart=results_pie_chart.render())


@app.route("/teams", methods=("GET", "POST"))
def teams_selection():
    teams = Reports.teams.get_all_team_names()
    if request.method == "POST":
        team_name = request.form["teams"]
        return redirect(url_for("team_details", team_name=team_name))
    return render_template("selection.html", names=teams)


@app.route("/players", methods=("GET", "POST"))
def players_selection():
    players = Reports.players.get_all_players_names()
    if request.method == "POST":
        players = fuzzy_filter_players(players, request.form["player"])
        print(request.form["player"])
    return render_template("player_selection.html", players=players)


@app.route("/players/<player_id>")
def player_details(player_id: str):
    player = Reports.players.get_player_by_id(player_id)
    awards = Reports.players.get_player_awards(player_id)
    stats = Reports.players.get_player_basic_stats(player_id)
    return render_template(
        "player_details.html", 
        player=player,
        goals_by_team=render_players_goals_by_team(Reports.players.get_player_goals_by_team(player_id)),
        awards=awards,
        stats=stats,
        appearances_by_tournament=render_player_appearances_by_tournament(Reports.players.get_matches_by_tournament(player_id))
    )


@app.route("/tournaments")
def tournaments():
    tournaments_list = Reports.tournaments.get_tournaments_list()
    
    return render_template(
        "tournaments.html",
        tournaments=tournaments_list,
        goals_by_tournament=render_goals_by_tournament(Reports.tournaments.get_goals_and_games_by_tournament()),
        top_scorers=Reports.tournaments.get_top_scorers(how_many=20)
        )



    

if __name__ == "__main__":
    app.run(debug=True)