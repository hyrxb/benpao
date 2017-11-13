#!/usr/bin/env python
# -*- coding:utf8 -*-

from multiprocessing import Process
import time

def start(name):
    time.sleep(1)
    print('hello',name)

if __name__ == '__main__':
    p = Process(target=start,args=('zhangshan',))
    p1 = Process(target=start,args=('lisi',))
    p.start()
    p1.start()
    p.join()
