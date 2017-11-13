#!/usr/bin/env python
# -*- coding:utf8 -*-

#进程间通信
from multiprocessing import Process,Queue

def start(q):
    q.put("hello")

if __name__ == '__main__':
    q =Queue()
    p = Process(target=start,args=(q,))
    p.start()
    print q.get()
    p.join()

