#!/usr/bin/env python
# -*- coding:utf8 -*-

import multiprocessing

def f(x):
    return x**2

pool = multiprocessing.Pool(5)
real = pool.map(f,[1,2,3,4,5,6,7,8,9,10])

print real