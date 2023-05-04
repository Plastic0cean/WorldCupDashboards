import pytest
from Db.DbTableFunction import DbTableFunction

def test_db_function_without_params():
    func = DbTableFunction("Test")
    assert func.select_statement() == "SELECT * FROM Test()"

def test_db_function_with_single_parameter():
    func = DbTableFunction("Test", "1")
    assert func.select_statement() == "SELECT * FROM Test('1')"

def test_db_function_with_dict_as_parameters_placeholder():
    params = {
        "param1": 1,
        "param2": "X"
        }
    func = DbTableFunction("Test", parameters=params)
    assert func.select_statement() == "SELECT * FROM Test(@param1='1', @param2='X')"

def test_db_with_default_params():
    func = DbTableFunction("Test", use_default_parameters=True)
    assert func.select_statement() == "SELECT * FROM Test(default)"

def test_db_function_with_desc_sort():
    func = DbTableFunction("Test")
    assert func.select_statement(sort_by="1", descending=True) == "SELECT * FROM Test() ORDER BY 1 DESC"

def test_db_function_with_order_by_and_limit():
    func = DbTableFunction("PlayersList")
    assert func.select_statement(limit=10, sort_by="1") == "SELECT TOP 10 * FROM PlayersList() ORDER BY 1"