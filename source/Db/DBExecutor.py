from Config import db_config
from DbConnection import DBConnection

def create_connection_string(driver: str, server: str, database: str) -> str:
    return "Driver={" + driver + "};" + f"Server={server};" + f"Database={database};" + "Trusted_Connection=yes;"

connection_string = create_connection_string(db_config.driver, db_config.server, db_config.database)
db_connection = DBConnection(connection_string)

    