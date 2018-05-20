from .tool.sperate import split_num
from .tool.combine import first_stack
from .db import conn_all
import numpy as np


def find_M(list):
    min0 = min(list)
    max0 = max(list)
    return min0,max0

def single_norm(list):
    min,max = find_M(list)
    new_list = []
    for i in list:
        new_list.append((i-min)/(max-min))
    return new_list

def all_norm(nlist):
    tmp = map(list,zip(*nlist))
    nlist_T = list(tmp)
    new_nlist = map(single_norm,nlist_T)
    new_nlist_T = map(list,zip(*new_nlist))
    return list(new_nlist_T)

def use_data(X_num,Y_num,pertime):
    #table = gen_data(X_num,Y_num,pretime)
    table = conn_all('dataBlock','`1560-5X-1Y-Y`','112.74.45.185',3306,'root','opal123456!@#').export()
    l = len(table)
    train_num,valid_num = split_num(l)
    norm_table = list(all_norm(table))
    print(norm_table[0][-1])
    new_table = np.array(norm_table)[:,1:]
    np.random.shuffle(new_table)
    T = [];V = [];flag = 1;flag1 = 1
    counter = 0
    for row in new_table:
        counter += 1
        if counter < train_num:
            T,flag = first_stack(T,row,flag)
        else:
            V,flag1 = first_stack(V,row,flag1)
    return T,V
