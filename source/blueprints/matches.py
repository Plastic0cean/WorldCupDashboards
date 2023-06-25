from flask import Blueprint, render_template, request
from Reports.matches import repository

matches = Blueprint("matches", __name__)


@matches.route("/matches")
def matches_list():
    matches = repository.get_list_of_matches_by_tournament("WC-2022")
    return render_template("matches_list.html", matches=matches)


@matches.route("/match-details/<match_id>")
def match_details(match_id: str):
    match = repository.get_by_id(match_id)
    events = repository.get_events(match_id)
    return render_template("match_details.html", events=events, match=match[0])