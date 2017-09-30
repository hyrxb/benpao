#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
import thread
import time

class QSBK:

	def __init__(self):
		self.pageIndex = 1
		self.user_agent = ''
		self.headers = {'User-Agent':self.user_agent}
		self.stories = []
		self.enable = False

	def getPage(self,pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib2.Request(url,headers=self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode
		except urllib2.URLError,e:
			if hasattr(e,"reason"):
				print u"connect error:",e.reason
				return None
	def getPageItems(self,pageIndex):
		