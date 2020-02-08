import pymysql
from config import Config

class Db:
    
    def __init__(self):
        try:
            self.connection = pymysql.connect(host=Config.host, port=Config.port, user=Config.user, passwd=Config.passwd, db=Config.db)
            self.cursor = self.connection.cursor()
        except BaseException as e:
            self.connection = pymysql.connect(host=Config.host, port=Config.port, user=Config.user, passwd=Config.passwd)
            self.cursor = self.connection.cursor()
        finally:
            print('Connection with mysql created succesfully <br>')

    def getQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getOneQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    
    def updateQuery(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def updateDataBase(self, sql):
        self.connection.db = None
        self.cursor.execute(sql)
        self.connection.commit()

    def updateTable(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

db = Db()