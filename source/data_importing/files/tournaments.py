import common

COLUMNS_TO_DELETE = ["key_id", "winner", "host_won", 'group_stage', 'second_group_stage', 
                     'final_round', 'round_of_16', 'quarter_finals', 'semi_finals', 'third_place_match', 
                     'final', "count_teams"]


def process():
    tournaments = common.read_dataset(common.DataSource.TOURNAMENTS)
    tournaments = common.delete_columns(tournaments, COLUMNS_TO_DELETE)
    common.import_to_db(tournaments, "tournaments")


if __name__ == "__main__":
    process()