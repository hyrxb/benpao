#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request('https://movie.douban.com/nowplaying/hangzhou')

resp = urllib2.urlopen(request)

html_data  =resp.read().decode('utf-8')

soup = BeautifulSoup(html_data,'html.parser')

nowplaying_movie = soup.find_all('div',id='nowplaying')

nowplaying_movie_list = nowplaying_movie[0].find_all('li',class_='list-item')

# print(nowplaying_movie_list)

nowplaying_list = []

for item in nowplaying_movie_list:
	nowplaying_dict = {}
	nowplaying_dict['id'] = item['data-subject']
	for tag_img_item in item.find_all('img'):
		nowplaying_dict['name'] = tag_img_item['alt']
		nowplaying_list.append(nowplaying_dict)

print nowplaying_list


requrl = 'https://movie.douban.com/subject/' + nowplaying_list[0]['id'] + '/comments' + '?start=0' + '&limit=20'
resp = urllib2.Request(requrl)
response = urllib2.urlopen(resp)
comment_data = response.read().decode('utf-8')
soup = BeautifulSoup(comment_data,'html.parser')
comment_div_lits = soup.find_all('div',class_='comment')
# print comment_div_lits

eachCommentList = []
for item in comment_div_list:
	if item.find_all('p')[0].string is not None:
		eachCommentList.append(item.find_all('p')[0].string)


comments = ''

for k in len(eachCommentList):
	comments = comments + (str(eachCommentList[k])).strip()
