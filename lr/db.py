import MySQLdb
#import MySQLdb.cursors as cursors

class conn_db(object):
    def __init__(self,host,port,user,psw,db,table):
        self.host = '120.39.63.241'
        self.port = 3306
        self.user = 'root'
        self.psw = 'sxl!123456'
        self.db = db
        self.table = table

    def export(self):
        try:
            conn = MySQLdb.connect(host = host,port = port,user = user,password = psw,db = db)
            cursor = conn.cursor()
            cursor.execute('select * from '+table)

            while 1:
                row = cursor.fetchone()
                if row:
                    yield row
                else:
                    break

        except ProgrammingError:
            print "Tried to read a cursor after it was already closed"
        finally:
            cursor.close();conn.close()
        #values = cursor.fetchall()#value is a tuple type:(str,str,datatime.datetime,int,int)
        #l=list(zip(*values))#tuple2zip2list
        #return l

class conn_rainfall(conn_db):
    def __init__(self,host,port,user,psw,db,table,inverval):
        super(conn_rainfall,self).__init__(host,port,user,psw,db,table)
        self.db = 'rainfall'
        self.interval = interval
    def export(self):
        super(conn_rainfall,self).export()
        conn = MySQLdb.connect(host = host,port = port,user = user,password = psw,db = db)
        cursor = conn.cursor()
        values = cursor.execute('select * from')

        values = cursor.fetchall()#value is a tuple type:(str,str,datatime.datetime,int,int)
        l=list(zip(*values))#tuple2zip2list

        cursor.close();conn.close()

class conn_device(conn_db):
    def __init__(self,host,port,user,psw,db,table):
        super(conn_rainfall,self).__init__(host,port,user,psw,db,table)
        self.db = 'device_monitor'
    def export(self,table):
        conn = MySQLdb.connect(host = host,port = port,user = user,password = psw,db = db)
        cursor = conn.cursor()
        values = cursor.execute('')

        values = cursor.fetchall()#value is a tuple type:(str,str,datatime.datetime,int,int)
        l=list(zip(*values))#tuple2zip2list

        cursor.close();conn.close()
