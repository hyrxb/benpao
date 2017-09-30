#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import threading
import re
from Queue import Queue
import urllib2

thread_count = 100
page = 50



class Cq(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.Q = queue
		self.headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0'}

	def run(self):
		while True:
			try:
				url = self.Q.get(True,1)
				self.spider(url)
			except:break

	def spider(self,url):
		#print "start url:%s" % url
		req  =urllib2.Request(url.encode('utf-8'),headers=self.headers)
		response = urllib2.urlopen(req)
		html = response.read()
		soup = BeautifulSoup(html,'html.parser')
		titiles = soup.find_all('th',attrs={'class':'forumtit'})
		print titiles



def Load_Thread(queue):
	return [Cq(queue) for i in range(thread_count)]


def Start_Thread(threads):
	print "thread is start....."
	for t in threads:
		t.setDaemon(True)
		t.start()
	for t in threads:
		t.join()
	print 'thread is end...'

def main():
	queue = Queue()
	for i in range(0,page):
		target = 'https://bbs.ichunqiu.com/forum-59-%s.html' %i
		queue.put(target)

	thread_list = Load_Thread(queue)
	Start_Thread(thread_list)

if __name__ =="__main__":
	main()