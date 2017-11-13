#!/usr/bin/env python
# -*- coding:utf8 -*-

import threading
import time
num = 100
lock = threading.Lock()
def show():
    global num
    time.sleep(1)
    lock.acquire() #修改前加锁
    num -=1
    lock.release() #修改后解锁

list = []
for i in range(100):
    t = threading.Thread(target=show)
    t.start()
    list.append(t)

for t in list:
    t.join()
    print t.getName() + '---' +str(num)

print num