#!/usr/bin/env python
#-*- coding:utf8 -*-

import csv

DATA = (
    (11,'12','12--1,12--2'),
    (21,'22','22--1,22--2,22--3'),
    (31,'32','32--1,32--2')
)

print('将数据写到csv')

f = open('test.csv','w')
