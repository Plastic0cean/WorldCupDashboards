from collections import defaultdict
from flask import Blueprint, render_template, request
from repository.matches import match_repository
from repository.tournaments import tournament_repository
from repository.squads import squads_repository


matches = Blueprint("matches", __name__)


def produce_match_events(events) -> dict:
    def default_value():
        return {"home_team": [], "away_team": []}
    result_events = defaultdict(default_value)
    for event in events:
        if event.home_team == 1:
            result_events[event.minute_label]["home_team"].append(event)
        else:
            result_events[event.minute_label]["away_team"].append(event)
    return dict(result_events)

def produce_matches_list(matches) -> dict:
    result = dict()
    for match in matches:
        if match.match_date in result:
            result[match.match_date].append(match)
        else:
            result[match.match_date] = [match]
    return result
            
@matches.route("/matches")
def matches_list():
    tournaments = tournament_repository.get_all()
    tournament_id = request.args.get('id', default="WC-2022")
    matches = match_repository.get_matches_results_by_tournament(tournament_id)
    matches = produce_matches_list(matches)
    selected_tournament = tournament_repository.get_by_id(tournament_id)
    return render_template(
        "matches_list.html", matches=matches,
        tournaments=tournaments, selected_tournament=selected_tournament)

@matches.route("/match/<match_id>")
def match_details(match_id: str):
    match = match_repository.get_result(match_id)
    events = match_repository.get_events(match_id)
    squads = squads_repository.get_team_squad_by_match(match_id)
    return render_template("match_details.html", events=events, match=match[0], squads=squads)