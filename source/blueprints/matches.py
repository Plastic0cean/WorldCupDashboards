from flask import Blueprint, render_template, request
from entities.match import MatchesSummaryCollection
from repository.match_event import events_repository
from repository.match_summary import match_summary_repository
from repository.tournaments import tournament_repository
from repository.squads import squads_repository


matches = Blueprint("matches", __name__)


@matches.route("/matches")
def matches_list():
    tournaments = tournament_repository.get_all()
    tournament_id = request.args.get('id', default="WC-2022")
    matches = MatchesSummaryCollection(match_summary_repository.get_by_tournament(tournament_id))
    selected_tournament = tournament_repository.get_by_id(tournament_id)
    return render_template(
        "matches_list.html", 
        matches=matches.to_dict(),
        tournaments=tournaments, 
        selected_tournament=selected_tournament)


@matches.route("/match/<match_id>")
def match_details(match_id: str):
    return render_template(
        "match_details.html", 
        events=events_repository.get_by_match(match_id), 
        match=match_summary_repository.get_by_id(match_id),
        home_team_squad=squads_repository.get_team_squad_by_match(match_id, True), 
        away_team_squad=squads_repository.get_team_squad_by_match(match_id, False)
        )