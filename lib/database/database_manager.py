import os
import sqlite3


CREATE_DB_SCRIPT = '''CREATE TABLE user_typing_data (
                          time timestamp NOT NULL default CURRENT_TIMESTAMP,
                          user_id integer NOT NULL,
                          input0 text NOT NULL,
                          IP text,
                          browser text,
                          PRIMARY KEY  (time, user_id)
                        );'''


class DatabaseManager:
    '''Manages database connections, executes scripts'''
    def __init__(self, path):
        '''Initializes sqlite3 database.

        Keyword arguments:
        path -- the path where database file is saved
        '''
        self.path = path

        if not os.path.exists(path):
            self.conn = sqlite3.connect(path)
            self.execute(CREATE_DB_SCRIPT)
        else:
            self.conn = sqlite3.connect(path)

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
