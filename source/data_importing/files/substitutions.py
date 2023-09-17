import common

COLUMNS_TO_DELETE = ["key_id", "tournament_name", 'match_name', 'match_date', 'stage_name', 'group_name',
                     "team_name", "team_code", 'team_name', 'team_code', 'home_team', 'away_team',
                     'family_name', 'given_name', 'shirt_number', 'family_name',
                     'given_name', 'shirt_number', 'minute_label'
                     ]

def process():
    substitutions = common.read_dataset(common.DataSource.SUBSTITUTIONS)
    substitutions = common.delete_columns(substitutions, COLUMNS_TO_DELETE)
    common.import_to_db(substitutions, "substitutions")


if __name__ == "__main__":
    process()