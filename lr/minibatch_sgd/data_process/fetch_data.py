from .tool.sperate import split_num
from .tool.combine import first_stack
import numpy as np


def find_M(array):
    min = np.min(array)
    max = np.max(array)
    return min,max

def single_norm(array):
    min,max = find_M(array)
    list = []
    for i in array:
        list.append((i-min)/(max-min))
    return np.array(list)

def all_norm(narray):
    nlist = map(single_norm,narray.T)
    return np.array(nlist).T

def use_data(X_num,Y_num,pertime):
    table = gen_data(X_num,Y_num,pretime)
    table = np.array(table)[:,1:]

    l = len(table)
    train_num,valid_num = split_num(l)

    norm_table = all_norm(table)
    np.random.shuffle(norm_table)
    T = [];V = [];flag = 1;flag1 = 1
    counter = 0
    for row in norm_table:
        counter += 1
        if counter%batchsize < train_num:
            T,flag = first_stack(T,row,flag)
        else:
            V,flag1 = first_stack(V,row,flag1)
    return T,V
