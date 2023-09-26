from .common import DataSource, delete_columns, import_to_db, read_dataset, rename_columns

COLUMNS_TO_DELETE = [
    "tournament_name", "award_name", "family_name", 
    "given_name", "team_id", "team_name", "team_code"
    ]

COLUMNS_MAPPING = {"key_id": "award_winners_id"}

def process():
    winners = read_dataset(DataSource.AWARD_WINNERS)
    winners = delete_columns(winners, COLUMNS_TO_DELETE)
    winners = rename_columns(winners, COLUMNS_MAPPING)
    import_to_db(winners, "award_winners")

if __name__=="__main__":
    process()