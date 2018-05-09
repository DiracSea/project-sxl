import csv
import numpy as np
import random
import matplotlib.pyplot as plt
#A is row vector
#X is column vector
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
    return (y-y_p)*(-X.T)

def db(y,y_p):#negative partial b/gradb
    return (y-y_p)*(-1)

def loss_func(A,b,X,y):#loss function
    tmp = y - (A*X + b)
    tmp = tmp**2
    SSE = sum(tmp) / (2*len(X))
    return SSE#sum of square error

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

def regular(X,y):
    X_max = X_array.max()
    X_min = X_array.min()
    tmp = np.ones(np.shape(X))*X_min
    X_tmp = X-tmp
    y_max = max(y)
    y_min = min(y) 
    if X_max != 0 and y_max != 0:
        for i in range(0,len(X)):
            X[i] = X_tmp[i]/(X_max - X_min)
            y[i] = (y[i] - y_min)/(y_max - y_min)
    elif X_max == 0 and y_max != 0:
        for i in range(0,len(X)):
            y[i] = (y[i] - y_min)/(y_max - y_min)
    elif y_max == 0:
        for i in range(0,len(X)):
            X[i] = X_tmp[i]/(X_max - X_min)
    else:
        pass
    return [X,y]


def iter_batch(X,y,batchsize,shuffle=False):#每次随机抽batchsize个样本
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

def train(X,y,A,b,all_loss,all_step,rate):
    loss = 0
    all_dA = np.zeros(np.shape(A))
    all_db = 0

    for i in xrange(0,len(X)):
        y_p = A*X[i] + b
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

def validate(Xt,yt,A,b):
    loss = 0
    for i in xrange(0,len(Xt)):
        yt_p = A*Xt[i] + b
        loss = loss + (yt[i] - yt_p)*(yt[i] - yt_p)/2
    loss = loss/len(Xt)
    return loss


def run(X,y,Xt,yt,A,b,epochs,batchsize=200):
    plt.figure()
    for n in xrange(epochs):
        all_loss = []
        all_step = []
        for batch in iter_batch(X,y,batchsize,shuffle=True):
            X_batch, y_batch = batch
            l_train,A,b,all_loss,all_step = train(X_batch, y_batch,A,b,all_loss,all_step,rate)

        l_val = validate(Xt, Yt, A, b)
        logging.info('epoch:' + str(n) + ' ,train_loss:' + str(l_train) + ' ,val_loss:' + str(l_val)
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.show()
    plt.close('all') 
    return A, b, l_train, l_val