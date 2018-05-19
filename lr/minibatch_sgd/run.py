from .minibatch import run_single,run_all

def select_func(condition):
    try:
        return {
            'rand_block': run_single,
            'single_block': run_single,
            'all_block': run_all
        }[condition]
    except KeyError:
        print('input condition is wrong')

def minibatch_run(table,db = 'dataBlock',condition='single_block',rate=0.1,A_scale=1,b_scale=1,batchsize=24):
    return select_func(condition)(A_scale,b_scale,batchsize,table,db,condition,rate)