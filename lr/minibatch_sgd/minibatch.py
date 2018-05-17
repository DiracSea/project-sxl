import numpy as np
import random
import matplotlib.pyplot as plt
import logging

from .data_process.slice_data import slice_single,slice_all
from .data_process.tool.combine import first_stack
#A is row vector
#X is column vector, rainfall
#y is water
#sparse training set
#shuffle data set
#consider 0 data
'''
rate = 0.2
A=[]
b=20
X #global X is array
'''
def dA(y,y_p,X):#negative partial A/gradA, A is vector
    return (y-y_p)*(-X)

def db(y,y_p):#negative partial b/gradb
    return (y-y_p)*(-1)

def scale(X,A_scale,b_scale,flag):
    flag = 0
    l = len(X[0])
    A = np.random.rand(l)*A_scale
    b = random.random()*b_scale
    return A,b,flag

def log(epochs,l_train,l_val):
    logging.info('epoch:' + str(epochs) + ' ,train_loss:' + str(l_train) + ' ,val_loss:' + str(l_val))

'''
def loss_func(A,b,X,y):#loss function
    tmp = y - (np.dot(A,X) + b)
    tmp = tmp**2
    SSE = sum(tmp) / (2*len(X))
    return SSE#sum of square error
'''


def train(X,y,A,b,rate,all_loss):#X, y is batch
    loss = 0
    all_dA = np.zeros(np.shape(A))
    all_db = 0

    for i in range(len(X)):
        y_p = np.dot(A,X[i]) + b
        loss = loss + (y[i] - y_p)*(y[i] - y_p)/2
        all_dA = all_dA + dA(y[i],y_p,X[i])
        all_db = all_db + db(y[i],y_p)
    
    loss = loss/len(X)
    all_loss.append(loss)
    A = A - rate*all_dA/len(X)
    b = b - rate*all_db/len(X)
    return A,b,all_loss

def validate(Xv,yv,A,b):
    loss = 0
    length = 0
    for i in range(len(Xv)):
        yv_p = np.dot(A,Xv[i]) + b
        loss = loss + (yv[i] - yv_p)*(yv[i] - yv_p)/2
        length+=1
    loss = loss/length
    return loss


def run_single(A_scale,b_scale,batchsize,table,condition,rate):#A,b is scale

    plt.figure()
    epochs = 0

    all_step = [];all_loss = []
    yv = np.array([])
    flag = 1;flag1 = 1;i = 0
    A = 0;b = 0;l_train = 0
    Xv = [];yv = np.array([])

    for X,y,Xt,yt in slice_single(batchsize,table,condition):
        #if i < 5:
        #    i+=1
            if flag:
                A,b,flag = scale(X,A_scale,b_scale,flag)

            Xv,flag1 = first_stack(X,Xt,flag1)
            yv = np.append(yv,yt)
            epochs+=1
            A,b,all_loss = train(X,y,A,b,rate,all_loss)

            all_step.append(epochs)
        

    l_val = validate(Xv, yv, A, b)
    l_train = sum(all_loss)/epochs
    log(epochs,l_train,l_val)

    plt.plot(all_step,all_loss,color='blue')
    plt.xlabel('step')
    plt.ylabel('loss')
    plt.show()

    return A,b,l_train,l_val

def run_all(A_scale,b_scale,batchsize,table,condition,rate):
    plt.figure()

    epochs = 0
    flag = 1;flag1 = 1
    Xv = [];yv = np.array([])
    A = 0;b = 0;l_train = 0;l_val = 0
    all_loss = []
    all_step = []
    
    for data,label in slice_all(table):
        if label == 'train':
            epochs+=1
            X = data[:,:-1]####
            y = data[:,-1]
            if flag:
                A,b,flag = scale(X,A_scale,b_scale,flag)
            A,b,all_loss = train(X,y,A,b,rate,all_loss)
            all_step.append(epochs)

        elif label == 'valid':
            Xv,flag1 = first_stack(Xv,data[:,:-1],flag1)
            yv = np.append(yv,data[:,-1])

    l_val = validate(Xv, yv, A, b)
    l_train = sum(all_loss)/epochs
    log(epochs,l_train,l_val)

    plt.plot(all_step,all_loss,color='blue')
    plt.xlabel('step')
    plt.ylabel('loss')
    plt.show()
    return A, b, l_train, l_val

