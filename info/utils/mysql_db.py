# coding=utf-8
import pymysql
import sys


class DatabaseHandle(object):
    """定义一个Mysql操作类"""

    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, self.port, charset='utf8')
        self.cursor = self.db.cursor()

    def insert_db(self, sql):
        self.cursor = self.db.cursor()

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print('Error: unable to insert,error:', sys.exc_info()[0])
        finally:
            last_id = self.cursor.lastrowid
            self.cursor.close()
            return last_id

    def delete_db(self, sql):
        self.cursor = self.db.cursor()

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print('Error: unable to delete,error:', sys.exc_info()[0])
        finally:
            self.cursor.close()

    def update_db(self, sql):
        self.cursor = self.db.cursor()

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print('Error: unable to update,error:', sys.exc_info()[0])
        finally:
            self.cursor.close()

    def fetchall(self, sql):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:
            print('Error: unable to fetch all data,error:', sys.exc_info()[0])
        finally:
            self.cursor.close()

    def fetchone(self, sql):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except:
            print('Error: unable to fetch one data,error:', sys.exc_info()[0])
        finally:
            self.cursor.close()

    def close_db(self):
        self.db.close()

db = DatabaseHandle("10.250.156.28", "slave", "5jiu4xiejirong", "yalla", port=3306)
