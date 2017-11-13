#!/usr/bin/env python
# -*- coding:utf8 -*-

stock = {
    "name":"GOOG",
    "shares":100,
    "price":490.10
}

name = stock["name"]
value = stock["shares"] * stock["price"]


prices = {
    "GOOG":490.10,
    "AAPL":123.50,
    "IBM":91.50,
    "MSFT":52.13
}


prices = dict()

if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0




for n in [1,2,3,4,5,6,7,8,9]:
    print "2 to the %d power is %d" %(n,2**n)


for n in range(1,10):
    print "2 to the %d power is %d" %(n,2**n)

a = range(5)
b=range(1,8)
c= range(0,14,3)
