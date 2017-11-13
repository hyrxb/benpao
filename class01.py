#!/usr/bin/env python
# -*- coding:utf8 -*-

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self,object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)

s = Stack()

s.push("Dave")
s.push(42)
s.push([3,4,5])

x = s.pop()
y = s.pop()

del s

