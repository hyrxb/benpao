#!/usr/bin/env python
# -*- coding:utf8 -*-

import time
import threading
def run(n):
    print("Hello..[%s]\n" %n)
    time.sleep(2)

def main():
    for i in range(5):
        t = threading.Thread(traget=run,args=[i,])
        t.start()
        t.join(1)

m = threading.Thread(target=main,args=[])
m.setDaemon(True)
m.start()
print("---done---")