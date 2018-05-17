import MySQLdb
import numpy as np

global cur;global conn
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
            cur = conn.cursor()
            #with conn.cursor() as cur:
            cur.execute('select * from '+self.table)

            while 1:
                row = cur.fetchone()#use fetchone but not fetchall
                if row:
                    yield np.array(row) #generate a generator
                else:
                    break

        except GeneratorExit:
            print("Tried to read a cursor after it was already closed")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
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
        super(conn_block,self).__init__(db,table,host,port,user,psw)

    def export(self):
        try:
            conn = MySQLdb.connect(host = self.host,port = self.port,user = self.user,password = self.psw,db = self.db)
            cur = conn.cursor()
            cur.execute('select * from '+self.table)
            flag1 = 1;flag3 = 0;label = 1;row = ()
            while flag1:
                block = []
                flag2 = 1
                if flag3:
                    flag3 = 0
                    block.append(row.tolist())
                while flag2:
                    row = cur.fetchone()#use fetchone but not fetchall

                    if row:
                        row = np.array(row)
                        if label != int(row[0]):
                            flag2 = 0;flag3 = 1
                            label = int(row[0])
                            yield block#generate block generator
                        else:
                            block.append(row.tolist())
                    else:
                        flag1 = 0
                        flag2 = 0
                
        except GeneratorExit:
            print("Tried to read a cursor after it was already closed")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

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