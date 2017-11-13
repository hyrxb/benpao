#!/usr/bin/env python
#-*- coding:utf8 -*-

def printinfo(name,age=35):
    print "Name:",name
    print "Age:",age
    return;


printinfo(age=50,name="miki")
printinfo(name="miki")


def printinfo1(arg1,*vartuple):
    print "输出"
    print arg1
    for var in vartuple:
        print var
    return;


printinfo1(10)
printinfo1(70,60,50)


sum = lambda arg1,arg2:arg1+arg2;

print "demo：",sum(10,20)
print "dmeo:",sum(20,20)
