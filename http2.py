#!/usr/bin/env python
#coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import random
import MySQLdb
import multiprocessing
import re

class Article(object):
    #构造函数初始化数据库链接
    def __init__(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306,db='xiaoshuo',charset='utf8')
        self.db.autocommit(True)
        self.db.set_character_set("utf8")
        self.cursor = self.db.cursor()

    #获取header头
    def getRandHeader(self):
        headers = [
            'NOKIA5700/ UCWEB7.0.2.37/28/999',
            'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
            'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
            'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
            'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
            'UCWEB7.0.2.37/28/999'
        ]
        return {'User-Agent': random.choice(headers)}

    #爬取网页内容
    def spiderUrl(self,url):
        req = urllib2.Request(url,headers=self.getRandHeader())
        print req
        res = urllib2.urlopen(req)
        html = res.read().decode("utf8")
        return html

    #获取小说正文部分
    def getContent(self,queue):
        url = queue.get() #获取队列里的url
        # print url
        html = self.spiderUrl(url)
        soup = BeautifulSoup(html,"lxml")
        title = soup.find('div',id='main_body').find('h1').text
        print title
        soup_text = soup.find('div',id='content')
        print soup_text
        sql = "insert into article(title,url,content)value('%s','%s','%s')" %(title,url,soup_text)
        print sql
        #self.cursor.execute(sql)
        #print soup_text

    #爬取章节，把章节信息入库
    def getZanjie(self,url):
        html = self.spiderUrl(url)
        soup = BeautifulSoup(html,'lxml')
        soup_text = soup.find('div',id='book_detail',class_='box1').find_next('div')
        for link in soup_text.ol.children:
            if link != '\n':
                print link.text
                sql = "insert into article_title(title,url) value ('%s','%s')" %(link.text,link.a.get('href'))
                print sql
                print self.cursor.execute(sql)

    #获取要爬取的url
    def getQueueUrl(self):
        sql = "SELECT url from article_title where status = 0 limit 2"
        self.cursor.execute(sql)
        urls = self.cursor.fetchall()
        for url in urls:
            queue = multiprocessing.Queue()
            queue.put(url[0])  #返回的url是个元组,取小标为0的url
            p1 = multiprocessing.Process(target=self.getContent,args=(queue,))
            p1.start()
            print p1.name
            p1.join()




if __name__ =='__main__':
    article = Article()
    #爬取章节
    # url = 'http://www.136book.com/huaqiangu/'
    # article.getZanjie(url)
    #爬取内容
    # url = 'http://www.136book.com/huaqiangu/ebxeew/'
    # article.getContent(url)
    #while True:
    article.getQueueUrl()
