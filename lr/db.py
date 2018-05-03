import MySQLdb
import csv

class conn_db(object):
    def __init__(self,host,port,user,psw,db):
        self.host = '120.39.63.241'
        self.port = 3306
        self.user = 'root'
        self.psw = 'sxl!123456'
        self.db = db
    def export(self):
        pass

class conn_rainfall(conn_db):
    def __init__(self,host,port,user,psw,db,inverval):
        super(conn_rainfall,self).__init__(self,host,port,user,psw,db)
        self.db = 'rainfall'
        self.interval = interval
    def export(self,interval):
        conn = MySQLdb.connect(host,port,user,psw,db)
        cursor = conn.cursor()
        cursor.execute('')

        cursor.close();conn.close()

class conn_device(conn_db):
    def __init__(self,host,port,user,psw,db):
        super(conn_rainfall,self).__init__(self,host,port,user,psw,db)
        self.db = 'device_monitor'
    def export(self):
        conn = MySQLdb.connect(host,port,user,psw,db)
        cursor = conn.cursor()
        cursor.execute('')

        cursor.close();conn.close()
