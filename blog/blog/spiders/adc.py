#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import os
from blog.items import BlogItem

class AdcSpider(scrapy.Spider):
	name = 'adc'
	allowed_domains=['www.shaimn.com']
	start_urls = ['http://www.shaimn.com/xinggan/']


	# def parse(self,response):
	# 	current_url = response.url
	# 	body = response.body
	# 	unicode_body = response.body_as_unicode()
	# 	print(unicode_body)

	def parse(self,response):
		#print response.body
		items = response.xpath('//div[@class="showlist"]/li')
		for item in items:
			blogitem = BlogItem()
			blogitem['url'] = item.xpath('//p[@class="showpic"]/a/@href').extract()
			blogitem['img'] = item.xpath('//p[@class="showpic"]/a/img/@src').extract()
			blogitem['title']= item.xpath('//p[@class="showpic"]/a/img/@alt').extract()
			yield blogitem
			

			# yield scrapy.Request(url=url,callback=self.parse) #递归爬取 
