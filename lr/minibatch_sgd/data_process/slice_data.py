from .read_data import read_all_block,read_rand_data,read_single_block

def select_func(condition):
    try:
        return {
            'rand_block': read_rand_data,
            'single_block': read_single_block
        }[condition]
    except KeyError:
        print('input condition is wrong')

#split data into training and validation set

def slice_single(batchsize, table, db, condition):
    for T, V in select_func(condition)(batchsize, table, db):
        length = len(T[1])

        X = T[:,:-1]
        X[:,-1] = X[:,-1]/1000
        y = T[:,-1]/1000
        Xt = V[:,:-1]
        Xt[:,-1] = Xt[:,-1]/1000
        yt = V[:,-1]/1000
        '''
        X = T[:,:-1]
        y = T[:,-1]
        Xt = V[:,:-1]
        yt = V[:,-1]
        '''
        yield X,y,Xt,yt#modified batch

def slice_all(table,db):
    for data, label in read_all_block(table,db):
        yield data, label
