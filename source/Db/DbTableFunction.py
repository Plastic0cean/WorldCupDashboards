from Db.DbConnection import conn

class DbTableFunction:
    """"
    The class represents SQL function which meants to return a table.
    It allows to perform a select operation over a function.
    If there is a need to call a SQL function from then default different schema, 
    add the schema name in {self.name} argument of __init__ method.
    >> DbTableFunction('[SchemaName].[TestFunction]')
    """
    
    def __init__(self, name: str, parameters=None, use_default_parameters: bool=False) -> None:
        self.name = name
        self._parameters = parameters
        self.use_default_parameters = use_default_parameters

    @property
    def parameters_str(self) -> str:
        params=""
        if self._parameters:
            if isinstance(self._parameters, dict):
                params = ", ".join([f"@{name}='{value}'" for name, value in self._parameters.items()])
            else:
                params = f"'{self._parameters}'"
            return params
        if self.use_default_parameters:
            params = "default"
        return params
        
    def select_statement(self, sort_by: str=None, descending: bool=False, limit: int=None):
        params = self.parameters_str
        top = f"TOP {limit} " if limit else ""
        query = f"SELECT {top}* FROM {self.name}({params})" 
        if sort_by:
            query+= f" ORDER BY {sort_by}"
            if descending:
                query+=" DESC"
        return query

    def select(self, conn, sort_by: str=None, descending: bool=False, limit: int=None):
        query = self.select_statement(sort_by=sort_by, descending=descending, limit=limit)
        with conn:
            result = conn.execute(query, get_results=True)
        return result
    
    def select_as_dict(self, conn, sort_by: str=None, descending: bool=False, limit: int=None):
        query = self.select_statement(sort_by=sort_by, descending=descending, limit=limit)
        with conn:
            result = conn.select_as_dict(query)
        return result