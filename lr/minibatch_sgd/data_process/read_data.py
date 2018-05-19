import numpy as np
import random
from .db import *
from .tool.combine import first_stack
from .tool.sperate import split_num
#all array



def read_rand_data(batchsize,table,db):#yield batch  
    rand = conn_rand(db,table,'112.74.45.185',3306,'root','opal123456!@#')###
    counter = 0
    size = 0
    train_num, valid_num = split_num(batchsize)
    for row in rand.export():
        if size%batchsize == 0:
            T = [];V = [];flag = 1;flag1 = 1
        if row:
            row = np.array(row)
            counter += 1
            size += 1
            if size%batchsize != 0:
                if counter%batchsize < train_num:
                    T,flag = first_stack(T,row,flag)
                else:
                    V,flag1 = first_stack(V,row,flag1)
            else:
                yield T,V
        else:
            yield T,V

def del_label(table,db):
    block = conn_block(db,table,'112.74.45.185',3306,'root','opal123456!@#')###
    for b in block.export():
        a = np.array(b)
        yield a[:,1:]


def read_single_block(blank,table,db):
    for block in del_label(table,db):
        if block!= np.array([]):
            batchsize = len(block)
            train_num, valid_num = split_num(batchsize)
            T = [];V = [];flag = 1;flag1 = 1
            np.random.shuffle(block)
            counter = 0
            for row in block:
                counter += 1
                if counter%batchsize < train_num:
                    T,flag = first_stack(T,row,flag)
                else:
                    V,flag1 = first_stack(V,row,flag1)
            yield T,V#batch


def read_all_block(table,db):
    for block in del_label(table,db):
        if block!= np.array([]):
            seed = int(random.random()*10)
            if(seed < 7):
                yield block,"train"
            else:
                yield block,"valid"



