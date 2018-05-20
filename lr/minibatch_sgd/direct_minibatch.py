#this is minibatch algorithm which is rewrited from minibatch and read data directly from caoz
import datetime
import os
import numpy as np
import matplotlib.pyplot as plt
from .data_process.fetch_data import use_data
from .minibatch import scale,train,validate


def current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在

def divide(input):
    X = input[:,:-1]
    y = input[:,-1]
    return X,y

def rand_select_batch(T,batchsize):
    np.random.shuffle(T)
    return T[:batchsize,:]

def run(X_num,Y_num,pertime,A_scale,b_scale,batchsize,epochs,rate,name):

    flag = 1; all_step = []; train_loss = []; valid_loss = []

    T,V = use_data(X_num,Y_num,pertime,name)
    my_path = os.path.abspath(os.path.dirname(__file__))
    log_name = '_'+name+'_batch'+str(batchsize)+'_epochs'+str(epochs)+'_rate'+str(rate)+'_X'+str(X_num)+'_Y'+str(Y_num)+'_T'+str(pertime)
    path = os.path.join(my_path, "log\\"+'log'+log_name+'.txt')
    path1 = os.path.join(my_path, "plot\\")
    with open(path,'a+') as f:
        f.write('current_time:'+current_time()+'\n')
        f.write('batchsize:'+str(batchsize)+',epochs:'+str(epochs)+',rate:'+str(rate))
        f.write('X:'+str(X_num)+',Y:'+str(Y_num)+',per_time:'+str(pertime)+'\n')
        
    plt.figure()
    for i in range(epochs):
        batch = rand_select_batch(T,batchsize)
        X,y = divide(batch)
        if flag:
            A,b,flag = scale(X,A_scale,b_scale,flag)
        
        A,b,loss_t = train(X,y,A,b,rate)

        Xv,yv = divide(V)
        loss_v = validate(Xv,yv,A,b)

        all_step.append(i)
        train_loss.append(loss_t)
        valid_loss.append(loss_v)

        with open(path,'a') as f:
            f.write('epochs:'+str(i)+',train_loss:'+str(loss_t)+',validation_loss:'+str(loss_v)+'\n')

    plt.plot(all_step,train_loss,color = 'blue',label = 'train')
    plt.plot(all_step,valid_loss,color = 'red', label = 'validation')
    plt.xlabel('step')
    plt.ylabel('loss')
    plt.legend()
    plt.savefig(path1+'plot'+log_name+'.png')####

    l_train = sum(train_loss)/epochs
    l_val = loss_v

    with open(path,'a') as f:
        f.write('A:'+str(A)+',b:'+str(b)+'\n')
        f.write('l_train:'+str(l_train)+',l_valid:'+str(l_val)+'\n')

    print('A:',A)
    print('b:',b)
    print('l_train:',l_train)
    print('l_val:',l_val)
    return A,b,l_train,l_val
    