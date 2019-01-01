from twisted.enterprise.adbapi import ConnectionPool
from hodl_db.schema import Column


class Query:
    pass


class Session:
    encrypt = False  # TODO: encryption

    def __init__(self, filename='main.sqlite'):
        self.dbpool = ConnectionPool("sqlite3", filename, check_same_thread=False)

    async def query(self, base, filter_by=None, first=False):
        pass


class Base(type):
    __tablename__ = None
    _columns = {}

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._columns = {
            key: val for key, val in cls.__dict__.items() if isinstance(val, Column)
        }
