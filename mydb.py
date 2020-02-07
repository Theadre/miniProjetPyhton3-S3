import pymysql
from config import Config

class Db:
    
    def __init__(self):
        self.connection = pymysql.connect(host=Config.host, port=Config.port, user=Config.user, passwd=Config.passwd, db=Config.db)
        self.cursor = self.connection.cursor()

    def getQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getOneQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    
    def updateQuery(self, sql, params = ('info', '2019')):
        self.cursor.execute(sql)
        self.connection.commit()

    def updateDataBase(self, sql):
        connection = pymysql.connect(host=Config.host, port=Config.port, user=Config.user, passwd=Config.passwd)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    def updateTable(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

