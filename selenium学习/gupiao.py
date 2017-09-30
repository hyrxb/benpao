#!/usr/bin/env python
# -*- coding:utf-8 -*-


import urllib2
from bs4 import BeautifulSoup
import re
import time
import os

def getHtml(url,headers):

	#request  =urllib2.Request(url),headers=headers)  error
	request  =urllib2.Request(url.encode('utf-8'),headers=headers)

	response = urllib2.urlopen(request)

	return response.read()



def getContent(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	html = getHtml(url,headers)
	soup = BeautifulSoup(html,'html.parser')
	a = soup.find_all('a')
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

	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	pic_content = getHtml(src,headers)

	file_name  = os.path.join(imgPath,str(int(round(time.time() * 1000))) +'.jpg')
	print file_name

	with open(file_name,'wb') as f:
	  	f.write(pic_content)
	  	print('download end \n')

def getDetail(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/55.0','Referer':url}
	html = getHtml(url,headers)
	soup = BeautifulSoup(html,'html.parser')
	tag = soup.find('div',attrs={'class':'main-meta'})

	title = tag.find('a').text
	imgPath = '/home/alex/'+title.encode('utf-8')
	#print imgPath

	if not os.path.isdir(imgPath):
	 	os.mkdir(imgPath)

 	nav = soup.find('div',attrs={'class':'pagenavi'})
	nav = str(nav)
	result = re.findall(r"<span class=\"dots\">.*?</span><a.*?<span>(.*?)</span>",nav)
	end =  int(result[0])
	for i in range(1,end):
	 	src = url + '/' + str(i)
		savePic(src,imgPath)

    




url = 'http://www.mzitu.com'

urls = getContent(url)

for url in urls:
 	getDetail(url)

