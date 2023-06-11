from typing import Any, List
from collections import defaultdict
import pyodbc 
from Config import config


def create_connection_string(driver: str, server: str, database: str):
    return "Driver={" + driver + "};" + f"Server={server};" + f"Database={database};"+ "Trusted_Connection=yes;" + "MARS_Connection=yes;"


class Singleton:
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class DBConnection(Singleton):

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
        self.conn = None

    def _connect(self) -> None:
         self.conn = pyodbc.connect(self.connection_string)

    def execute(self, sql: str, get_results: bool=False):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if get_results:
            return cursor.fetchall()
        
    def execute_many(self, sql: str, values: List[Any]):
        cursor = self.conn.cursor()
        cursor.fast_executemany = True
        cursor.executemany(sql, values)

    def __enter__(self):
        if self.conn is None:
            self._connect()

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.conn.commit()
        # self.conn.close()

    def select_as_dict(self, sql: str) -> dict:
        result = defaultdict(list)
        query_result = self.execute(sql, get_results=True)
        try:
            fields = [field[0] for field in query_result[0].cursor_description]
            for values in query_result:
                for field, value in zip(fields, values):
                    result[field].append(value)
            return dict(result)
        except IndexError:
            return dict()
        

conn = DBConnection(create_connection_string(config.db.driver, config.db.server, config.db.database))