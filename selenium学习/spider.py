#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


class Spider:
	
	def __init__(self,url):
		self.url = url

	def getHtml(self):
		return urllib2.urlopen(self.url).read()

	def getContent(self):
		html = self.getHtml()
		print html


spider = Spider('https://bohaishibei.com/post/category/main/')
spider.getContent()


