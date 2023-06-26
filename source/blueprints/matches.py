from collections import defaultdict
from flask import Blueprint, render_template
from Reports.matches import repository

matches = Blueprint("matches", __name__)

def produce_match_events(events) -> dict:
    def default_value():
        return {"home_team": [], "away_team": []}
    result_events = defaultdict(default_value)
    for event in events:
        if event.home_team == "1":
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
    matches = repository.get_list_of_matches_by_tournament("WC-2022")
    matches = produce_matches_list(matches)
    return render_template("matches_list.html", matches=matches)

@matches.route("/match-details/<match_id>")
def match_details(match_id: str):
    match = repository.get_by_id(match_id)
    events = produce_match_events(repository.get_events(match_id))
    return render_template("match_details.html", events=events, match=match[0])