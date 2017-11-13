#!/usr/bin/env python
# -*- coding:utf8 -*-

import multiprocessing as multipro

def proc1(pipe):
    pipe.send('hello')
    print('proc1 recv:',pipe.recv())

def proc2(pipe):
    print("proc2 recv:",pipe.recv())
    pipe.send('hello,too')

pipe = multipro.Pipe()
p1 = multipro.Process(target=proc1,args=(pipe[0],))
p2 = multipro.Process(atrget=proc2,args=(pipe[1],))

p1.start()
p2.start()
p1.join()
p2.join()
