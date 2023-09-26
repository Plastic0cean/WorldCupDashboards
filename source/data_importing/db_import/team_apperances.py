from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = [
    'key_id', 'tournament_name', 'match_name', 'stage_name', 
    'group_name', 'group_stage', 'knockout_stage', 'replayed',
    'replay', 'match_date', 'match_time', 'stadium_id', 'stadium_name',
    'city_name', 'country_name', 'team_name', 'team_code',
    'opponent_name', 'opponent_code', 'goal_differential', 'extra_time', 
    'penalty_shootout', 'penalties_for', 'penalties_against', 'result'
    ]

def process():
    matches = read_dataset(DataSource.TEAM_APPEARANCES)
    matches = delete_columns(matches, COLUMNS_TO_DELETE)
    import_to_db(matches, "team_appearances")


if __name__ == "__main__":
    process()