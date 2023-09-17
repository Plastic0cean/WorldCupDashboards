import common

COLUMNS_TO_DELETE = ["key_id"]

def process():
    awards = common.read_dataset(common.DataSource.AWARDS)
    awards = common.delete_columns(awards, COLUMNS_TO_DELETE)
    common.import_to_db(awards, "awards")

if __name__=="__main__":
    process()
