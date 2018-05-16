import MySQLdb
#import MySQLdb.cursors as cursors

class conn_db(object):
    def __init__(self,db,table,host,port,user,psw):
        self.host = host
        self.port = port
        self.user = user
        self.psw = psw
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
            print("Tried to read a cursor after it was already closed")
        finally:
            cursor.close();conn.close()
        #values = cursor.fetchall()#value is a tuple type:(str,str,datatime.datetime,int,int)
        #l=list(zip(*values))#tuple2zip2list
        #return l
#1
class conn_rand(conn_db):#yield row
    def __init__(self,db,table,host,port,user,psw):
        super(conn_db,self).__init__(db,table,host,port,user,psw)
        
    def export(self):
        super(conn_db,self).export()
#2
class conn_block(conn_db):#yield block
    def __init__(self,db,table,host,port,user,psw):
        super(conn_single_block,self).__init__(db,table,host,port,user,psw)

    def export(self):
        try:
            conn = MySQLdb.connect(host = self.host,port = self.port,user = self.user,password = self.psw,db = self.db)
            cursor = conn.cursor()
            cursor.execute('select * from '+self.table)
            flag1 = 1
            label = 1
            row = ()
            while flag1:
                block = []
                flag2 = 1
                block.append(row)
                while flag2:
                    row = cursor.fetchone()#use fetchone but not fetchall
                    if row:
                        if label != row[0]:
                            flag2 = 0
                            label = row[0]
                            yield block#generate block generator
                        else:
                            block.append(row)
                    else:
                        flag1 = 0
                
        except ProgrammingError:
            print("Tried to read a cursor after it was already closed")
        finally:
            cursor.close();conn.close()

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