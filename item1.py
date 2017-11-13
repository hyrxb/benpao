#!/usr/bin/env python
#! -*- coding:utf8 -*-

stock = ('GOOG',100,490.10)
address = ('www.python.org',80)

first_name = 'Dave'
last_name = 'ChaLi'
person = (first_name,last_name)


item = 'aaa'

a = ()

b = (item,)
c= item,

print a
print b
print c


#jiebao

name,shares,price = stock;

host,port = address

first_name,last_name = person


filename = "portfolio.csv"

portfolio = []

for line in open(filename):
    fields = line.split(",")
    name = fields[0]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price)
    portfolio.append(stock)


s = set([3,5,9,10])
t=set("Hello")




