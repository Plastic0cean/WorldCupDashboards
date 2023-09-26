from .award_winners import process as award_winners
from .awards import process as awards
from .bookings import process as bookings
from .goals import process as goals
from .group_standings import process as group_standings
from .matches import process as matches
from .player_apperances import process as player_apperances
from .players import process as players
from .qualified_teams import process as qualified_teams
from .squads import process as squads
from .substitutions import process as substitutions
from .team_apperances import process as team_apperances
from .teams import process as teams
from .tournament_standings import process as tournament_standings
from .tournaments import process as tournaments

MODULES = [
    award_winners, awards, bookings, goals, group_standings, matches, player_apperances,
    players, qualified_teams, squads, substitutions, team_apperances, teams, tournament_standings, tournaments
]

for data_processing in MODULES:
    data_processing()
    
print("Successfully imported data to db")