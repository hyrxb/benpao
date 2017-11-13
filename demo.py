#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("/root/01.txt")
line = f.readline()
while line:
    print line,
    line = f.readline()
f.close()

for line in open("/root/01.txt"):
    print line,


f = open("/root/out.txt","w")
while year <= numyears:
    principal = principal *(1+ rate)
    print >>f,"%3d %0.2f" %(year,printcipal)
    year +=1
f.close()


import sys

sys.stdout.write("Enter your name!");

name = sys.stdin.readline()

