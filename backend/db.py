import json
from pprint import pprint
import configparser
import pymysql


class DB():
    def __init__(self):
        self.db_local = {
            'host': "localhost",
            'user': "agulbs",
            'password': "agulbs",
            'database': "FundedFuturesNetwork",
            'cursorclass':  pymysql.cursors.DictCursor
        }
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = pymysql.connect(**self.db_local)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.cursor.close()
            self.conn.close()
        except AttributeError:  # isn't closable
            print('Not closable.')
            return True  # exception handled successfully

    def query(self, qry, params):
        try:
            self.cursor.execute(query, list(params.values()))
            res = self.cursor.fetchall()
            self.conn.close()
        except Exception as e:
            return str(e)

        return res


    def commit(self, qry, params):
        try:
            self.cursor.execute(qry, list(params.values()))
            self.conn.commit()
        except Exception as e:
            return str(e)

        return 1