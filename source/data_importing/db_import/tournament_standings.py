from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = ["key_id", "tournament_name", "team_name", "team_code"]

def process():
    tournament_standings = read_dataset(DataSource.TOURNAMENT_STANDINGS)
    tournament_standings = delete_columns(tournament_standings, COLUMNS_TO_DELETE)
    import_to_db(tournament_standings, "tournament_standings")


if __name__ == "__main__":
    process()