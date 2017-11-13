#!/usr/bin/env python
# -*- coding:utf8 -*-

def divide(a,b):
    q = a/b
    r = a -q*b
    return(q,r)

import div

a,b = div.divide(2305,29)

