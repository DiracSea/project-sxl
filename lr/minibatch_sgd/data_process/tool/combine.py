import numpy as np

def first_stack(X1,X2,flag):
    if flag:
        flag = 0
        X1 = X2
    else:
        X1 = np.row_stack((X1,X2))
    return X1,flag



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