from twisted.enterprise.adbapi import ConnectionPool


class Session:
    encrypt = False  # TODO: encryption

    def __init__(self, filename='main.sqlite'):
        self.dbpool = ConnectionPool("sqlite3", filename, check_same_thread=False)

    async def query(self, base, filter_by=None, first=False):
        pass


class Base(type):
    pass
