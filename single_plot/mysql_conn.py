# import mysql driver:
#import mysql.connector;mysql-python#cannot use

import MySQLdb
import matplotlib.pyplot as plt#draw graph



def single_sewer(i):
    conn = MySQLdb.connect(host = '120.79.208.59',port=3306,user='sulongze', password='258369Aa', db='device_monitordb')#
    cursor = conn.cursor()

    cursor.execute("select * from sensor"+str(i))
    values = cursor.fetchall()#value is a tuple type:(str,str,datatime.datetime,int,int)
    l=list(zip(*values))#tuple2zip2list

    #graph info
    Title = 'sensor_code:'+l[0][0]+';terminal_id:'+l[1][0]
    x = l[2]; y = l[3]
    xLabel = 'Time'; yLabel = 'Height'

    #draw
    fig = plt.figure()
    plt.plot(x,y)#plot
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(Title)
    plt.grid()
    plt.gcf().autofmt_xdate()
    #plt.show()
    plt.savefig('sensor_code'+l[0][0]+'_'+str(i)+'.png')
    plt.close('all')
    cursor.close();conn.close()

