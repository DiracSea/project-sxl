mini-bacth sgd user document
====
- [mini-bacth sgd user document](#mini-bacth-sgd-user-document)
    - [main：使用](#main)
    - [structure 内部结构说明:](#structure)
        - [connect_db: 连接数据库](#connect-db)
        - [data_process: 数据处理](#data-process)
        - [minibatch-sgd: 算法](#minibatch-sgd)
## main：使用

structure 内部结构说明:
----
### connect_db: 连接数据库 
包含若干用于连接不同种类数据库表格的类

* 父类，conn_db，基础连接功能的实现，在输入数据库相关信息并实例化后，调用export，逐行读取，返回的是一个generator
* 子类，conn_rand，完全继承conn_db，用于连接随机打乱的数据表格
* 子类，conn_block，重写了export方法，用于连接分块的数据表格
### data_process: 数据处理
分为两部分，读取数据和分割数据

1. read_data:
    * <pre><code>split_num(batchsize):return train_num,valid_num.</code></pre>
        <p>输入batchsize并计算出这个batchsize中对应的训练集数据大小和验证集数据大小</p>

    * <pre><code>read_rand_data(batchsize,table):yield T,V.</code></pre>
        <p></p>
    * <pre><code>del_label(table):yield A.</code></pre>
        <p></p>
    * <pre><code>read_single_block(blank,table):yield T,V</code></pre>
        <p></p>
    * <pre><code>read_all_block(table):yield block,label</code></pre>
        <p></p>
2. slice_data:
    * <pre><code>select_func(condition):return{}</code></pre>
        <p></p>
    * <pre><code>slice_rand(batchsize,table,condition):yield X,y,Xt,yt</code></pre>
        <p></p>
    * <pre><code>slice_all(table):yield data,label</code></pre>
        <p></p>
### minibatch-sgd: 算法
主要包含了minibatch-sgd 以及一些辅助功能的实现

* <pre><code>dA(y,y_p,X):return gradA</code></pre>
    <p></p>
* <pre><code>db(y,y_p):return gradb</code></pre>
    <p></p>
* <pre><code>loss_func(A,b,X,y):return SSE</code></pre>
    <p></p>
* <pre><code>shuffle_data(X,y):return [X,y]</code></pre>
    <p></p>
* <pre><code>train(X,y,A,b,all_loss,all_step,rate):return A,b,loss,all_loss,all_step</code></pre>
    <p></p>
* <pre><code>validate(Xv,yv,A,b):return loss</code></pre>
    <p></p>
* <pre><code>run(A,b,batchsize,table,condition,rate):return A,b,l_train,l_val</code></pre>
    <p></p>
* <pre><code>run_all(A,b,table,condition,rate):A,b,l_train,l_val</code></pre>
    <p></p>

