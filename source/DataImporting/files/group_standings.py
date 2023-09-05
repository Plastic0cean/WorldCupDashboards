import common

COLUMNS_TO_DELETE = ["key_id", "team_name", "team_code", "tournament_name", "goal_difference"]

def process():
    standings = common.read_dataset(common.DataSource.GROUP_STANDINGS)
    standings = common.delete_columns(standings, COLUMNS_TO_DELETE)
    common.import_to_db(standings, "group_standings")

if __name__ == "__main__":
    process()