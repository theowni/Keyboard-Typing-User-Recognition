import os
import sqlite3


PATH = os.path.dirname(os.path.abspath(__file__))
CREATE_DB_SCRIPT = os.path.join(
    os.path.dirname(PATH),
    'db_sql/create_db.sql'
)


class DatabaseManager:
    '''Manages database connections, executes scripts'''
    def __init__(self, path):
        '''Initializes sqlite3 database.

        Keyword arguments:
        path -- the path where database file is saved
        '''
        self.path = path
        self.conn = sqlite3.connect(path)

        if not os.path.exists(path):
            self.run_sql_from_file(CREATE_DB_SCRIPT)

    def run_sql_from_file(self, path):
        '''Executes specified by path script'''
        with open(path) as f:
            script = f.read()

        self.conn.execute(script)

    def execute(self, command):
        '''Executes specified sql command'''
        return self.conn.execute(command)

    def open(self):
        '''Opens database connection'''
        self.conn = sqlite3.connect(self.path)

    def close(self):
        '''Closes database connection'''
        self.conn.close()
