#!/usr/bin/env python
# -*- coding:utf-8 -*-


import urllib2
from bs4 import BeautifulSoup
import re
import time
import os

def getHtml(url,headers):

	#request  =urllib2.Request(url),headers=headers)  error
	#这里需要对url请求地址进行编码，不然会报错
	request  =urllib2.Request(url.encode('utf-8'),headers=headers)

	response = urllib2.urlopen(request)

	return response.read()



def getContent(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	html = getHtml(url,headers)
	soup = BeautifulSoup(html,'html.parser')
	a = soup.find_all('a') #查询所有的a标签
	lst = []
	for i in a:
		href = i.attrs['href']
		ress = re.findall(r"\d+$",href)
		if len(ress):
			lst.append(href);
	return lst


def savePic(url,imgPath):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	html = getHtml(url,headers)
	soup = BeautifulSoup(html,'html.parser')
	div = soup.find('div',attrs={'class':'main-image'})
	img  = div.find('img')
	src =  img.attrs['src']
	#妹子图有防盗链，这里设置了referer
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	#抓取图片内容
	pic_content = getHtml(src,headers)
	#图片路径
	file_name  = os.path.join(imgPath,str(int(round(time.time() * 1000))) +'.jpg')
	print file_name
	#保存图片到本地
	with open(file_name,'wb') as f:
	  	f.write(pic_content)
	  	print('download end \n')

def getDetail(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	html = getHtml(url,headers)
	soup = BeautifulSoup(html,'html.parser')
	tag = soup.find('div',attrs={'class':'main-meta'})
	#查找妹子图片标签
	title = tag.find('a').text
	#按标签类型创建图片目录
	imgPath = '/home/alex/'+title.encode('utf-8')
	#print imgPath
	#判断目录是否存在
	if not os.path.isdir(imgPath):
	 	os.mkdir(imgPath)

 	nav = soup.find('div',attrs={'class':'pagenavi'})
	nav = str(nav) #转换成字符串
	#查找最后一个分页的页码数
	result = re.findall(r"<span class=\"dots\">.*?</span><a.*?<span>(.*?)</span>",nav)
	end =  int(result[0])
	#遍历生成分页地址
	for i in range(1,end):
	 	src = url + '/' + str(i)
		#下载图片
		savePic(src,imgPath)

    




url = 'http://www.mzitu.com'

urls = getContent(url)

for url in urls:
 	getDetail(url)

