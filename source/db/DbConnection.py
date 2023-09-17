from collections import defaultdict
from typing import Any, Optional
from Config import config
import sqlalchemy


class DBConnection:

    def __init__(self, host: str, user: str, password: str, db: str, port: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = db
        self.port = port
        self.conn = None

    def _connect(self) -> None:
        engine = sqlalchemy.create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(self.user, self.password, self.host, self.port, self.database))
        self.conn = engine.connect()

    @property
    def connected(self) -> bool:
        return self.conn is not None

    def execute(self, sql: str, parameters: dict=None, get_output: bool=True):
        try:
            if parameters is None: 
                output = self.conn.execute(sqlalchemy.text(sql))
            else:   
                output = self.conn.execute(sqlalchemy.text(sql), parameters)
            if get_output:
                return output.fetchall()
        except:
            self.conn.rollback()
            raise
        
    def __enter__(self) -> None:
        if not self.connected:
            self._connect()

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        self.conn.commit()
        self.conn.close()
        self.conn = None

    def select_as_dict(self, sql: str, parameters: dict=None):
        result = defaultdict(list)
        output = self.execute(sql, parameters)
        try:
            fields = output[0]._fields
            for values in output:
                for field, value in zip(fields, values):
                    result[field].append(value)
            return dict(result)
        except IndexError:
            return dict()


class StoredProcedure:

    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self._parameters = kwargs
        
    @property
    def _parameters_str(self) -> str:
        return ", ".join([f":{key}" for key in self._parameters.keys()])
    
    @property
    def _sql_code(self) -> str:
        return f"CALL {self.name} ({self._parameters_str})"

    def call(self, connection: DBConnection, get_output: bool=True):
        with connection:
            result = connection.execute(self._sql_code, self._parameters)
        if get_output:
            return result
        
    def to_dict(self, connection: DBConnection) -> dict:
        with connection:
            return connection.select_as_dict(self._sql_code, self._parameters)


conn = DBConnection(config.db.host, config.db.user, config.db.password, config.db.database, config.db.port)