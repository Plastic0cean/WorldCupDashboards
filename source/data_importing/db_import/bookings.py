from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = [
     "key_id", "tournament_id", "tournament_name", "match_name", "group_name",
     "family_name", "given_name", "match_date", "team_id", "team_name", "team_code", 
     "home_team", "away_team", "shirt_number", "stage_name", "minute_label",
     "match_period"
     ]


def process():
    bookings = read_dataset(DataSource.BOOKINGS)
    bookings = delete_columns(bookings, COLUMNS_TO_DELETE)
    import_to_db(bookings, "bookings")

if __name__=="__main__":
    process()
