from db import *
from minibatch-sgd import *

def read_data():
    rain = conn_db('rainfall','rainfall','',0,'','')
    device = conn_db('clone_device','xxx','',0,'','')
    for row in rain.export():
        
        yield row
    for row in device.export():
        
        pass

def slice_data():
    return X,y,Xt,yt