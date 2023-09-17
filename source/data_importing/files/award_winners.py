import common

COLUMNS_TO_DELETE = [
    "tournament_name", "award_name", "family_name", 
    "given_name", "team_id", "team_name", "team_code"
    ]

COLUMNS_MAPPING = {"key_id": "award_winners_id"}

def process():
    winners = common.read_dataset(common.DataSource.AWARD_WINNERS)
    winners = common.delete_columns(winners, COLUMNS_TO_DELETE)
    winners = common.rename_columns(winners, COLUMNS_MAPPING)
    common.import_to_db(winners, "award_winners")

if __name__=="__main__":
    process()