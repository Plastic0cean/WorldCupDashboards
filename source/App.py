from flask import Flask, render_template, request, redirect, url_for
from Visualizations.plots import * 
import Reports.players
import Reports.teams as teams
import Reports.tournaments as tournament
from SearchingEngine.Searching import fuzzy_filter_players

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")


@app.route("/teams/<team_id>", methods=("GET", "POST"))
def team_details(team_id: str):
    team = teams.get_team_by_id(team_id)
    goals_and_matches = teams.get_goals_and_matches_summary(team_id)
    win = teams.get_biggest_win(team_id)
    defeat = teams.get_biggest_defeat(team_id)
    scorers = teams.get_top_scorers(team_id, 10)
    results_pie_chart = PieChartPX(
        teams.get_matches_results(team_id),
        ["DarkBlue", "Red", "Green"], None)
    position_by_tournament = Reports.teams.get_position_by_tournaments(team_id)
    return render_template(
        "team_detals.html",
        team=team,
        goals_and_matches=goals_and_matches,
        win=win,
        defeat=defeat,
        scorers=scorers,
        results_chart=results_pie_chart.render(),
        position_by_tournament=position_by_tournament,
        goals_by_opponent=team_goals_by_opponent(teams.get_goals_by_opponent(team_id)),
        goals_by_tournament=team_goals_by_tournament(teams.get_goals_by_tournament(team_id)),
        most_minutes_by_player=players_with_most_minutes(teams.get_minutes_played_by_players(team_id)),
        matches_chart=all_matches_by_team(teams.get_list_of_matches(team_id)))


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
        appearances_by_tournament=player_appearances_by_tournament(Reports.players.get_matches_by_tournament(player_id)),
        appearances_summary = Reports.players.get_apperances_summary(player_id),
        minutes_played = overall_minutes_played(Reports.players.get_minutes_played(player_id)),
        starer_or_sub = starter_or_substitute(Reports.players.get_number_of_games_as_starter(player_id))
    )


@app.route("/tournaments")
def tournaments():
    tournament_id = request.args.get('id', default=None)
    tournaments_list = tournament.get_tournaments_list()
    most_goals_in_single_game=tournament.get_most_goals_in_single_game(tournament_id)
    most_cards_in_single_game=tournament.get_most_cards_in_single_game(tournament_id)
    top_scorers = tournament.get_top_scorers(tournament_id=tournament_id, how_many=20)
    goals_by_tournament = render_goals_by_tournament(tournament.get_goals_and_games_by_tournament())
    goals_by_minutes = goals_by_minute_hist(tournament.get_goals_by_minutes(tournament_id))
    goals_difference = goals_difference_by_team_bubble(tournament.get_goals_difference_by_team(tournament_id))
    
    return render_template(
        "tournaments.html",
        tournaments=tournaments_list,
        goals_by_tournament=goals_by_tournament,
        top_scorers=top_scorers,   
        most_goals_in_single_game=most_goals_in_single_game,
        most_cards_in_single_game=most_cards_in_single_game,
        tournament_id=tournament_id,
        # stadiums_map = show_stadiums_on_map(tournaments.get_number_of_matches_on_stadiums(tournament_id)),
        goals_by_minutes=goals_by_minutes,
        goals_difference=goals_difference
        )



    

if __name__ == "__main__":
    app.run(debug=True)