

class Db:
    
    
    @staticmethod
    def serverConnexion():
        db = pymysql.connect("localhost","root","")
        
    @staticmethod
    def databaseConnexion():
        db = pymysql.connect("localhost","root","groupef")
        