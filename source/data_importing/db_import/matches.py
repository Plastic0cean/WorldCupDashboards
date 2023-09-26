from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = [
    "key_id", "tournament_name", "stadium_name", "city_name", "country_name",
    "home_team_name", "home_team_code", "away_team_name", "away_team_code", "score",
    "home_team_score_margin", "away_team_score_margin", "score_penalties", "result", "match_name",
    "group_name", "group_stage", "replayed", "replay", "knockout_stage"
]


def process():
    matches = read_dataset(DataSource.MATCHES)
    matches = delete_columns(matches, COLUMNS_TO_DELETE)
    import_to_db(matches, "matches")

if __name__ == "__main__":
    process()
