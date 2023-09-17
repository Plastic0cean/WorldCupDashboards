import common

COLUMNS_TO_DELETE = ["key_id", "tournament_name", "team_name", "team_code"]

def process():
    tournament_standings = common.read_dataset(common.DataSource.TOURNAMENT_STANDINGS)
    tournament_standings = common.delete_columns(tournament_standings, COLUMNS_TO_DELETE)
    common.import_to_db(tournament_standings, "tournament_standings")


if __name__ == "__main__":
    process()