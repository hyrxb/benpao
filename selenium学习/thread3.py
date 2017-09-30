#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

class MyThread(threading.Thread):

	def __init(self,target,args):
		super(MyThread,self).__init__()
		self.target = target
		self.args = args

	def run(self):
		self.target(self.args)



def print_time(counter):
	while counter:
		print "counter = %d" % counter
		counter -= 1
		time.sleep(1)

def main():
	my_thread = MyThread(print_time, 10)
	my_thread.start()
	my_thread.join()


if __name__ == '__main__':
	main()