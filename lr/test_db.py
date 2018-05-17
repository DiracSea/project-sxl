from minibatch_sgd.data_process.db import *
import numpy as np

c = conn_db('dataBlock','`1560-5X-1Y-Y`','112.74.45.185',3306,'root','opal123456!@#')
for b in c.export():
    print(b[0])


'''
block = conn_block('dataBlock','`1560-5X-1Y-Y`','112.74.45.185',3306,'root','opal123456!@#')###
for b in block.export():
    a = np.array(b)
    print(a[:,1:])

'''