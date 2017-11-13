#!/usr/bin/env python
# -*- coding:utf8 -*-

def line_conf():
    def line(x):
        return 2 *x +1
    return line


myline = line_conf()
print myline(5)