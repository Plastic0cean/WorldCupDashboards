from dataclasses import dataclass


@dataclass
class DbConfig:
    server: str = r"(localdb)\ProjectsV13"
    driver: str = "ODBC Driver 17 for SQL Server"
    database: str = ""

    def read_file(path: str):
        pass


db_config = DbConfig()