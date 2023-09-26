from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = ["key_id", "tournament_name", "team_name", "team_code"]

def process():
    teams = read_dataset(DataSource.QUALIFIED_TEAMS)
    teams = delete_columns(teams, COLUMNS_TO_DELETE)
    import_to_db(teams, "qualified_teams")

if __name__ == "__main__":
    process()
