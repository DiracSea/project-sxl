from db import *
import numpy as np
import random
#all array

def read_rand_data(batchsize):#yield batchd  
    rand = conn_rand()###
    counter = 0
    size = 0
    train_num = int(batchsize*7/10+1/2)
    valid_num = batchsize - train_num
    for row in rand.export():
        if size%batchsize == 0：
            T = [];V = []
        if row:
            row = np.array(row)
            counter += 1
            size += 1
            if size%batchsize != 0:
                if counter%batchsize < train_num:
                    T.append(row)
                else:
                    V.append(row)
            else:
                yield T,V
        else:
            yield T,V
        
def read_single_block():
    single_block = conn_block()###
    for block in single_block.export():
        block = np.array(block)
        batchsize = len(block)
        train_num = int(batchsize*7/10+1/2)
        valid_num = batchsize - train_num
        T = [];v = []
        np.random.shuffle(block)
        counter = 0
        for row in block:
            counter += 1
            if counter%batchsize < train_num:
                T.append(row)
            else:
                V.append(row)
        yield T,V


def read_all_block():
    all_block = conn_block()###
    for block in all_block.export():
        block = np.array(block)
        seed = int(random.random()*10)
        if(seed < 7):
            yield block,"train"
        else:
            yield block,"valid"


    return data

def slice_data():

    return X,y,Xt,yt