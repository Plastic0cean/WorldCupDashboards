from .common import DataSource, delete_columns, import_to_db, read_dataset

COLUMNS_TO_DELETE = ["key_id"]

def process():
    awards = read_dataset(DataSource.AWARDS)
    awards = delete_columns(awards, COLUMNS_TO_DELETE)
    import_to_db(awards, "awards")

if __name__=="__main__":
    process()
