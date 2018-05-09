import MySQLdb
#import MySQLdb.cursors as cursors

#Parent
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
            conn = MySQLdb.connect(host = self.host,port = self.port,user = self.user,password = self.psw,db = self.db)
            cursor = conn.cursor()
            cursor.execute('select * from '+self.table)

            while 1:
                row = cursor.fetchone()#use fetchone but not fetchall
                if row:
                    yield row #generate a generator
                else:
                    break

        except ProgrammingError:
            print "Tried to read a cursor after it was already closed"
        finally:
            cursor.close();conn.close()
        #values = cursor.fetchall()#value is a tuple type:(str,str,datatime.datetime,int,int)
        #l=list(zip(*values))#tuple2zip2list
        #return l

'''
#Subclass 1
class conn_rainfall(conn_db):
    def __init__(self,host,port,user,psw,db,table):
        super(conn_rainfall,self).__init__(host,port,user,psw,db,table)
        self.db = 'rainfall'
    def export(self):
        super(conn_rainfall,self).export()

#Subclass 2
class conn_device(conn_db):
    def __init__(self,host,port,user,psw,db,table):
        super(conn_rainfall,self).__init__(host,port,user,psw,db,table)
        self.db = 'device_monitor'
    def export(self):
        super(conn_device,self).export()
'''