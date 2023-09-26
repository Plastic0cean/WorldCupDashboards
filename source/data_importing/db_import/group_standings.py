from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = ["key_id", "team_name", "team_code", "tournament_name", "goal_difference"]

def process():
    standings = read_dataset(DataSource.GROUP_STANDINGS)
    standings = delete_columns(standings, COLUMNS_TO_DELETE)
    import_to_db(standings, "group_standings")

if __name__ == "__main__":
    process()