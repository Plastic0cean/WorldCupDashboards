import common

COLUMNS_TO_DELETE = ["key_id", "tournament_name", "team_name", "team_code",
                     'family_name', 'given_name', 'shirt_number', "position_code"]

COLUMNS_MAPPING = {"position_name": "position"}

def process():
    squads = common.read_dataset(common.DataSource.SQUADS)
    squads = common.delete_columns(squads, COLUMNS_TO_DELETE)
    squads = common.rename_columns(squads, COLUMNS_MAPPING)
    common.import_to_db(squads, "squads")

if __name__ == "__main__":
    process()