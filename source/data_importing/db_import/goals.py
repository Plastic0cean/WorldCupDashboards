from .common import read_dataset, DataSource, delete_columns, import_to_db, rename_columns

COLUMNS_TO_DELETE = [
    "key_id", "away_team", "family_name", "given_name", "shirt_number",
    "player_team_name", "player_team_code", "minute_label", "tournament_id",
    "tournament_name", "match_name", "match_date", "stage_name", "group_name",
    "team_name", "team_code", "home_team"
]

COLUMNS_MAPPING = {"team_id": "opponent_id"}


def process():
    goals = read_dataset(DataSource.GOALS)
    goals = rename_columns(goals, COLUMNS_MAPPING)
    goals = delete_columns(goals, COLUMNS_TO_DELETE)
    import_to_db(goals, "goals")


if __name__ == "__main__":
    process()
