#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

for i in range(page,0,-1):
	target = 'https://bbs.ichunqiu.com/forum-59-%s.html' %i
	queue.put(target)

soup = BeautifulSoup(html,'html.parser')

res = soup.find_all(name='img',attrs={'alt':'heatlevel'})

for i in res:
	for j in i.parent.contents:
		if str(i).startswith('<a'):
			print j['href'],j.text
			link = 'https://bbs.ichunqiu.com/' + j['href']
			break


