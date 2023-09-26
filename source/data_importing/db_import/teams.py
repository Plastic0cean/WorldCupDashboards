from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = ["key_id", "federation_wikipedia_link", "confederation_id", "team_wikipedia_link"]

def process():
    teams = read_dataset(DataSource.TEAMS)
    teams = delete_columns(teams, COLUMNS_TO_DELETE)
    import_to_db(teams, "teams")


if __name__ == "__main__":
    process()