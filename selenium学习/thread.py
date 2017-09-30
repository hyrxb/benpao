#!/usr/bin/env python
# -*- coding:utf-8 -*-

import thread
import time


def print_time(thread_name,delay):
	count  = 0
	while count <5:
		time.sleep(delay)
		count +=1
		print "%s: %s" %(thread_name,time.ctime(time.time()))


try:
	thread.start_new_thread(print_time,('Thread-1',2))
	thread.start_new_thread(print_time,('Thread-2',4))
except:
	print "Error : unable to start the thread"

while True:
	pass
