import numpy as np
import random
from connect_db.db import *
#all array

def split_num(batchsize):
    train_num = int(batchsize*7/10+1/2)
    valid_num = batchsize - train_num
    return train_num, valid_num

def read_rand_data(batchsize,table):#yield batch  
    rand = conn_rand('dataBlock',table,'112.74.45.185',3306,'root','opal123456!@#')###
    counter = 0
    size = 0
    train_num, valid_num = split_num(batchsize)
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

def del_label(table):
    block = conn_block('dataBlock',table,'112.74.45.185',3306,'root','opal123456!@#')###
    for b in block.export():
        A = np.delete(b, 0, 1)
        yield A

def read_single_block(blank,table):
    for block in del_label(table):
        block = np.array(block)
        batchsize = len(block)
        train_num, valid_num = split_num(batchsize)
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

def read_all_block(table):
    for block in del_label(table):
        block = np.array(block)
        seed = int(random.random()*10)
        if(seed < 7):
            yield block,"train"
        else:
            yield block,"valid"



