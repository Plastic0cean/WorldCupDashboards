from flask import Flask, render_template, request, redirect, url_for
from Visualizations.plots import PieChartPX, players_goals_by_team, player_appearances_by_tournament
from Visualizations.plots import PieChartPX, players_goals_by_team, player_appearances_by_tournament, render_goals_by_tournament, show_stadiums_on_map
import Reports.teams 
import Reports.players
import Reports.tournaments
from SearchingEngine.Searching import fuzzy_filter_players

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")


@app.route("/teams/<team_id>", methods=("GET", "POST"))
def team_details(team_id: str):
    ranking = Reports.teams.get_goal_ranking_by_team(team_id)
    win = Reports.teams.get_biggest_win_by_team(team_id)
    defeat = Reports.teams.get_biggest_defeat_by_team(team_id)
    scorers = Reports.teams.get_top_scorers(team_id, 10)
    results_pie_chart = PieChartPX(
        Reports.teams.get_team_matches_summary(team_id),
        ["DarkBlue", "Red", "Green"], "Overall results of games played")
    return render_template(
        "team_detals.html",
        team_id=team_id,
        ranking=ranking,
        win=win,
        defeat=defeat,
        scorers=scorers,
        results_chart=results_pie_chart.render())


@app.route("/teams", methods=("GET", "POST"))
def teams_selection():
    teams = Reports.teams.get_all_team_names()
    if request.method == "POST":
        team_id = request.form["teams-dropdown"]
        return redirect(url_for("team_details", team_id=team_id))
    return render_template("selection.html", teams=teams)


@app.route("/players", methods=("GET", "POST"))
def players_selection():
    players = Reports.players.get_all_players_names()
    if request.method == "POST":
        players = fuzzy_filter_players(players, request.form["player"])
    return render_template("player_selection.html", players=players)


@app.route("/players/<player_id>")
def player_details(player_id: str):
    player = Reports.players.get_player_by_id(player_id)
    awards = Reports.players.get_player_awards(player_id)
    stats = Reports.players.get_player_basic_stats(player_id)
    return render_template(
        "player_details.html", 
        player=player,
        goals_by_team=players_goals_by_team(Reports.players.get_player_goals_by_team(player_id)),
        awards=awards,
        stats=stats,
        appearances_by_tournament=player_appearances_by_tournament(Reports.players.get_matches_by_tournament(player_id))
    )


@app.route("/tournaments")
def tournaments():
    tournament_id = request.args.get('id', default=None)
    print(tournament_id)
    print(tournament_id is None, tournament_id == "")

    tournaments_list = Reports.tournaments.get_tournaments_list()
    most_goals_in_single_game=Reports.tournaments.get_most_goals_in_single_game(tournament_id)
    most_cards_in_single_game=Reports.tournaments.get_most_cards_in_single_game(tournament_id)
    top_scorers = Reports.tournaments.get_top_scorers(tournament_id=tournament_id, how_many=20)
    goals_by_tournament=render_goals_by_tournament(Reports.tournaments.get_goals_and_games_by_tournament())
    
    
    return render_template(
        "tournaments.html",
        tournaments=tournaments_list,
        goals_by_tournament=goals_by_tournament,
        top_scorers=top_scorers,   
        most_goals_in_single_game=most_goals_in_single_game,
        most_cards_in_single_game=most_cards_in_single_game,
        tournament_id=tournament_id,
        stadiums_map = show_stadiums_on_map(
        Reports.tournaments.get_number_of_matches_on_stadiums(tournament_id))
        )



    

if __name__ == "__main__":
    app.run(debug=True)