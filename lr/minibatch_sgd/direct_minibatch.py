#this is minibatch algorithm which is rewrited from minibatch and read data directly from caoz
import datetime
import numpy as np
import matplotlib.pyplot as plt
from .data_process.fetch_data import use_data
from minibatch import scale,train,valid


def current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在

def divide(input):
    X = input[:,:-1]
    y = input[:,-1]
    return X,y

def rand_select_batch(T,batchsize):
    np.random.shuffle(T)
    return T[:batchsize,:]

def run(X_num,Y_num,pertime,A_scale,b_scale,batchsize,epochs,rate):

    flag = 1; all_step = []; train_loss = []; valid_loss = []

    T,V = use_data(X_num,Y_num,pertime)
    with open('log/log.txt','a') as f:
        f.write('current_time:'current_time()+'\n')
        f.write('X:'+str(X_num)+',Y:'+str(Y_num)+',per_time:'+str(pertime)+'\n')
        
    plt.figure()
    for i in range(epochs):
        if flag:
            A,b,flag = scale(T,A_scale,b_scale,flag)

        batch = rand_select_batch(T)
        X,y = divide(batch)
        A,b,loss_t = train(X,y,A,b,rate)

        Xv,yv = divide(V)
        loss_v = valid(Xv,yv,A,b)

        all_step.append(i)
        train_loss.append(loss_t)
        valid_loss.append(loss_v)

        with open('log/log.txt','a') as f:
            f.write('epochs:'+str(i)+',train_loss:'+str(train_loss)+',validation_loss:'+str(valid_loss)+'\n')

    plt.plot(all_step,train_loss,color = 'blue')
    plt.plot(all_step,valid_loss,color = 'red')
    plt.xlabel('step')
    plt.ylabel('loss')
    plt.savefig('plot/plot_X'+str(X_num)+'_Y'+str(Y_num)+'_time'+str(pertime)+'.png')####

    l_train = sum(train_loss)/epochs
    l_val = loss_v

    with open('log/log.txt','a') as f:
        f.write('A:'+str(A)+',b:'+str(b)+'\n')
        f.write('l_train:'+str(l_train)+',l_valid:'+str(l_valid)+'\n')

    print('A:',A)
    print('b:',b)
    print('l_train:',l_train)
    print('l_val:',l_val)
    return A,b,l_train,l_val
    