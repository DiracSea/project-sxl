import csv
import numpy as np
import random
import matplotlib.pyplot as plt
from data_process.slice_data import slice_rand,slice_all
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
'''
def loss_func(A,b,X,y):#loss function
    tmp = y - (np.dot(A,X) + b)
    tmp = tmp**2
    SSE = sum(tmp) / (2*len(X))
    return SSE#sum of square error
'''

def shuffle_data(X,y):#randomize X and y,testing
    seed = random.random()
    random.seed(seed)
    random.shuffle(X.tolist())
    random.seed(seed)
    random.shuffle(y.tolist())
    X = np.array(X)
    y = np.array(y)
    return [X,y]

def shuffle_index(inputs):
    indices = np.arange(inputs.shape[0])
    np.randpm.shuffle(indices)
    return indices
''' 
def regular(X,y):
    X_max = X_array.max()
    X_min = X_array.min()
    tmp = np.ones(np.shape(X))*X_min
    X_tmp = X-tmp
    y_max = max(y)
    y_min = min(y) 
    if X_max != 0 and y_max != 0:
        for i in range(len(X)):
            X[i] = X_tmp[i]/(X_max - X_min)
            y[i] = (y[i] - y_min)/(y_max - y_min)
    elif X_max == 0 and y_max != 0:
        for i in range(len(X)):
            y[i] = (y[i] - y_min)/(y_max - y_min)
    elif y_max == 0:
        for i in range(len(X)):
            X[i] = X_tmp[i]/(X_max - X_min)
    else:
        pass
    return [X,y]


def iter_batch(X,y,batchsize,shuffle=False):#randomly choose batchsize's samples
    if shuffle:
        indices = shuffle_index(X)
    for start_idx in range(0,inputs.shape[0]-batchsize+1,batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx+batchsize]
        else:
            excerpt = slice(start_idx,start_idx+batchsize)
        yield X[excerpt], y[excerpt]

def norm():
    pass
'''
def train(X,y,A,b,all_loss,all_step,rate):
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
    all_step.append(step)
    plt.plot(all_step,all_loss,color='blue')

    A = A - rate*all_dA
    b = b - rate*all_db
    return A, b, loss, all_loss, all_step

def validate(Xv,yv,A,b):
    loss = 0
    length = 0
    for X1,y1 in zip(Xv,yv):
        for Xt,yt in zip(X1,y1):
            yt_p = np.dot(A,Xt[i]) + b
            loss = loss + (yt[i] - yt_p)*(yt[i] - yt_p)/2
            length+=1
    loss = loss/length
    return loss


def run_single(A_scale,b_scale,batchsize,table,condition,rate):#A,b is scale
    plt.figure()
    epochs = 0
    Xv = []; yv = []
    all_loss = []
    all_step = []
    flag = 1
    for X,y,Xt,yt in slice_rand(batchsize,table,condition):
        if flag:
            flag = 0
            l = len(X[0])
            A = np.random.rand(l)*A_scale
            b = random.random()*b_scale
        Xv.append(Xt); yv.append(yt);epochs+=1
        l_train,A,b,all_loss,all_step = train(X, y,A,b,all_loss,all_step,rate)

    l_val = validate(Xv, yv, A, b)
    logging.info('epoch:' + str(n) + ' ,train_loss:' + str(l_train) + ' ,val_loss:' + str(l_val)
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.show()
    plt.close('all') 
    return A, b, l_train, l_val

def run_all(A_scale,b_scale,batchsize,table,condition,rate):
    plt.figure()
    epochs = 0;flag = 1
    Xv = [];yv = []
    all_loss = []
    all_step = []
    for data,label in slice_all(table):
        if flag:
            flag = 0
            l = len(X[0])
            A = np.random.rand(l)*A_scale
            b = random.random()*b_scale
        if label == 'train':
            epochs+=1
            X = data[:,:-1]####
            y = data[:,-1]
            l_train,A,b,all_loss,all_step = train(X, y,A,b,all_loss,all_step,rate)

        elif label == 'valid':
            Xv.append(data[:,:-1])####
            yv.append(data[:,-1])
    l_val = validate(Xv, yv, A, b)
    logging.info('epoch:' + str(n) + ' ,train_loss:' + str(l_train) + ' ,val_loss:' + str(l_val)
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.show()
    plt.close('all') 
    return A, b, l_train, l_val

