#!/usr/bin/enc python
# -*- coding:utf-8 -*-

import threading,thread
import time

class MyThread(threading.Thread):
	'''docstring for MyThread'''

	def __init__(self,thread_id,name,couter):
		super(MyThread,self).__init__()
		self.thread_id = thread_id
		self.name = name
		self.couter = couter

	def run(self):
		print "Starting " + self.name
		print_time(self.name,self.couter,5)
		print "Exiting " + self.name

def print_time(thread_name,delay,couter):
	while couter:
		time.sleep(delay)
		print "%s %s" %(thread_name,time.ctime(time.time()))
		couter -=1

def main():
	thread1 = MyThread(1,"Thread-1",1)
	thread2 = MyThread(2,"Thread-2",2)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()
	print "Exiting Main Thread"

if __name__ == '__main__':
	main()
