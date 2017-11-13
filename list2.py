#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
if len(sys.argv) !=2:
    print "Please supply a filename"
    raise SystemExit(1)

f = open(sys.argv[1])
lines = f.readlines()
print lines
f.close()