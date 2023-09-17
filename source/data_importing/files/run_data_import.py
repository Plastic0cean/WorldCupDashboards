import award_winners
import awards
import bookings
import goals
import group_standings
import matches
import player_apperances
import players
import qualified_teams
import squads
import substitutions
import team_apperances
import teams
import tournament_standings
import tournaments

MODULES = [
    award_winners, awards, bookings, goals, group_standings, matches, player_apperances,
    players, qualified_teams, squads, substitutions, team_apperances, teams, tournament_standings, tournaments
]

for data in MODULES:
    data.process()
print("Successfully imported data to db")