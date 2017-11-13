#coding:utf-8
from urllib import urlopen
import re
from urlparse import urljoin
from bs4 import BeautifulSoup
host ="http://www.525heart.com/index/index/index.html"

text = urlopen(host).read()

soup = BeautifulSoup(text,'html.parser')

for tag in soup(a):
    link = tag.attrs['href']
    link