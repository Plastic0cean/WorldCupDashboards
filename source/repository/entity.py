from db.DbConnection import DBConnection

class EntityRepository:
    """
    This is a base class for every other repository to inherit from.
    Altough, they can only inherit the constructor because other method can be 
    different for every single repository.
    """

    def __init__(self, conn: DBConnection) -> None:
        self.conn = conn