#!/usr/bin/env python
# -*- coding:utf8 -*-

filename = "test_file.txt"

def write_file():
    f = open(filename,'w')
    f.write('hello ithomer')
    f.write('\n')
    f.write('my blog:http://blog.ithomer.net')
    f.write('\n')
    f.write('this is the end')
    f.write('\n')
    f.close()


def read_file():
    f = open(filename,'r')
    line = f.readline()
    while line:
        print line
        line  =f.readline()
    f.close()


if __name__ =="__main__":
    write_file()
    read_file()