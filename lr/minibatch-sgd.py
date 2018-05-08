import csv
import numpy as np
import random
#A is row vector
#X is column vector
class minibatch_sgd(object):
    def __init__(self,rate):
        self.rate

rate = 0.2
A=[]
b=20
X #global X is array


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

def regular(X,y):
    X_max = X_array.max()
    X_min = X_array.min()
    tmp = np.ones(np.shape(X))*X_min
    X_tmp = X-tmp
    y_max = max(y)
    y_min = min(y)
    for i in range(0,len(X)):
        X[i] = X_tmp[i]/(X_max - X_min)
        y[i] = (y[i] - y_min)/(y_max - y_min)
    return [X,y]

def shuffle_index(inputs):
    indices = np.arange(inputs.shape[0])
    np.randpm.shuffle(indices)
    return indices

def iter_batch(X,y,batchsize,shuffle=False):
    if shuffle:
        indices = shuffle_index(X)
    for start_idx in range(0,inputs.shape[0]-batchsize+1,batchsize):
        if shuffle:
            excerpt = indices[start_idx:start_idx+batchsize]
        else:
            excerpt = slice(start_idx,start_idx+batchsize)
        yield X[excerpt], y[excerpt]


def f_train(A,b,step,bacth=200):
    all_loss = []
    all_step = []
    last_a = A
    last_b = b

    for step in range(1,step):
        loss = 0
        all_dA = np.zeros(np.shape(A))
        all_db = 0
        [X,y] = shuffle_data(X,y)



        for i in range(0,len(X_new)):
            y_p = A*X_new[i] + b
            loss = loss + (y_new[i] - y_p)*(y_new[i] - y_p)/2
            all_dA = all_dA + dA(y_new[i],y_p,X_new[i])
            all_db = all_db + db(y_new[i],y_p)
        loss = loss/len(X_new)
        #fig loss
        all_loss.append(loss)
        all_step.append(step)
        plt.plot(all_step,all_loss,color='orange')
        plt.xlabel("step")
        plt.ylabel("loss")

        last_a = A
        last_b = b
        A = A - rate*all_dA
        b = b - rate*all_db

        if step%1 == 0:
            print("step: ", step, " loss: ", loss)
            plt.show()

def loss_plot():
    pass

def f_val():
    pass

def run(X,y,Xt,yt,epochs,batchsize):
    for n in xrange(epochs):
        for batch in iter_batch(X,y,batchsize,shuffle=True):
            X_batch, y_batch = batch
            l_train, acc_train = f_train(x_batch, y_batch)

        l_val, acc_val = f_val(Xt, Yt)
        logging.info('epoch ' + str(n) + ' ,train_loss ' + str(l_train) + ' ,acc ' + str(acc_train) + ' ,val_loss ' + str(l_val) + ' ,acc ' + str(acc_val))