#TODO:
#1. Different ways to deal with existing tables/data
#3. Test how does it work with quoted fields (the 'corrupted' rows should be escaped)
import string
from typing import List


class DataLoader:

    def __init__(self, columns: List[str], table_name: str, dtypes: str) -> None:
        self.columns = columns
        self.table_name = table_name
        self.dtypes = dtypes 

    @staticmethod
    def clean_columns_names(columns: List[str], forbidden_characters=string.ascii_letters) -> List[str]:
        for column in columns:
            for char in forbidden_characters:
                column = column.replace(char, "")
        return columns

    def _create_table_code(self) -> str:
        columns_str = ", ".join(["[" + column + "] " + self.dtypes for column in self.columns])
        statement = f"""CREATE TABLE [{self.table_name}] (
            {columns_str});""" 
        return statement

    def create_table(self, conn) -> None:
        with conn:
            sql = self._create_table_code()
            conn.execute(sql)

    def _insert_code(self) -> str:
        column_str = ", ".join([f"[{column}]" for column in self.columns])
        placeholders = ", ".join("?" for _ in self.columns)
        sql = f"""
        INSERT INTO [{self.table_name}] ({column_str})
        VALUES
        ({placeholders});
        """
        return sql

    def insert(self, conn, values: List[str]) -> None:
        sql = self._insert_code()
        with conn:
            conn.execute_many(sql, values)


