#!/usr/bin/env python
#-*- coding:utf8 -*-

#一个进程下可以启动多个线程，多个线程共享父进程的内存空间，每个线程可以访问同一份数据，
# 所以当多个线程同时要修改同一份数据时，就会出现错误

import threading
import time
num = 100
def show():
    global num
    time.sleep(1)
    num -=1
    # print num

list=[]
for i in range(100):
    t=threading.Thread(target=show)
    t.start()
    list.append(t)

for t in list:
    t.join()
    print t.getName()
    print num
print num

