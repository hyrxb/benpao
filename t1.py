#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import threading
import multiprocessing

def worker(sign,lock):
    lock.acquire()
    print(sign,os.getpid())
    lock.release()

print('Main:',os.getpid())


record = []
lock = threading.Lock()
for i in range(5):
    thread = threading.Thread(target=worker,args=('thread',lock))
    thread.start()
    record.append(thread)

for thread in record:
    print(thread)
    thread.join()

record = []

lock = multiprocessing.Lock()
for i in range(5):
    process = multiprocessing.Process(target=worker,args=('process',lock))
    process.start()
    record.append(process)

for process in record:
    print process
    process.join()
