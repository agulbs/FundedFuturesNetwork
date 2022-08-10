import json
from pprint import pprint
import configparser
import pymysql


class DB():
    def __init__(self):
        self.db_local = {
            'host': "47.16.165.232",
			'user': "agulbs",
			'password': "alek07652",
			'db': "FundedFuturesNetwork",
			'cursorclass': pymysql.cursors.DictCursor
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
            self.cursor.execute(qry, list(params.values()))
            res = self.cursor.fetchall()
        except Exception as e:
            return str(e)

        return res


    def commit(self, qry, params):
        try:
            pprint(list(params.values()))
            self.cursor.execute(qry, list(params.values()))
            self.conn.commit()
        except Exception as e:
            return str(e)

        return 1
