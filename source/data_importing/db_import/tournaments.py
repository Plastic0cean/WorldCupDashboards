from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = ["key_id", "winner", "host_won", 'group_stage', 'second_group_stage', 
                     'final_round', 'round_of_16', 'quarter_finals', 'semi_finals', 'third_place_match', 
                     'final', "count_teams"]


def process():
    tournaments = read_dataset(DataSource.TOURNAMENTS)
    tournaments = delete_columns(tournaments, COLUMNS_TO_DELETE)
    import_to_db(tournaments, "tournaments")


if __name__ == "__main__":
    process()