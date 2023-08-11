import common

COLUMNS_TO_DELETE = ["key_id", "tournament_name", "team_name", "team_code"]

def process():
    teams = common.read_dataset(common.DataSource.QUALIFIED_TEAMS)
    teams = common.delete_columns(teams, COLUMNS_TO_DELETE)
    common.import_to_db(teams, "qualified_teams")

if __name__ == "__main__":
    process()
