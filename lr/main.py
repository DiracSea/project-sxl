from minibatch_sgd.run import minibatch_run as M
from minibatch_sgd.direct_minibatch import run

'''
A, b, l_train, l_val = M('`1560-5X-1Y-Y`','dataBlock','all_block',0.002,1,1,24)

A, b, l_train, l_val = M('`4410-5X-1Y-Y`','dataBlock','all_block',0.02,1,1,24)

print('A:',A)
print('b:%10.3f,l_train:%10.3f,l_val%10.3f'%(b,l_train,l_val))
'''
run(5,1,10,1,1,100,1000,0.01,'1560-5X-1Y-Y')
