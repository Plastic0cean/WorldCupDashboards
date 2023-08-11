import common

COLUMNS_TO_DELETE = ["key_id", "federation_wikipedia_link", "confederation_id"]

def process():
    teams = common.read_dataset(common.DataSource.TEAMS)
    teams = common.delete_columns(teams, COLUMNS_TO_DELETE)
    common.import_to_db(teams, "teams")


if __name__ == "__main__":
    process()