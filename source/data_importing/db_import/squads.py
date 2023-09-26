from .common import DataSource, delete_columns, import_to_db, read_dataset, rename_columns

COLUMNS_TO_DELETE = ["key_id", "tournament_name", "team_name", "team_code",
                     'family_name', 'given_name', 'shirt_number', "position_code"]

COLUMNS_MAPPING = {"position_name": "position"}

def process():
    squads = read_dataset(DataSource.SQUADS)
    squads = delete_columns(squads, COLUMNS_TO_DELETE)
    squads = rename_columns(squads, COLUMNS_MAPPING)
    import_to_db(squads, "squads")

if __name__ == "__main__":
    process()