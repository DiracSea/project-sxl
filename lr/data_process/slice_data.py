from read_data import read_all_block,read_rand_data,read_single_block

def select_func(condition):
    try:
        return {
            'batch': read_rand_data,
            'single_block': read_single_block
        }[condition]
    except KeyError:
        print 'input condition is wrong'

#split data into training and validation set

def slice_rand(batchsize, table, condition = 'batch'):
    for T, V in select_func(condition)(batchsize, table):
        X = T[]####
        y = T[-1]
        Xt = V[]
        yt = V[-1]
        yield X,y,Xt,yt

def slice_all(table):
    for data, label in read_all_block(table):
        yield data, label
