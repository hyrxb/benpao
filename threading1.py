#!/usr/bin/env python
#-*- coding:utf8 -*-

import threading
import time

def hello(name):
    print "Hello %s" %name
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=hello,args=("zhangshan",))
    t2 =threading.Thread(target=hello,args=("lisi",))

    t1.setName("aaa")
    t1.start()
    t2.start()
    t2.join()
    print("Hello")
    print(t1.getName())

