from socket import *

from time import ctime

print("=="*5)

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)

udpSerSock.bind(ADDR)

while True:
    print "等待接收消息..."
    data,addr = udpSerSock.recvfrom(BUFSIZ)

    udpSerSock.sendto('[%s]%s'%(ctime(),data),addr)
    print('response',addr)

udpSerSock.close()


#coding:utf8

from socket import *

HOST = '127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data)

udpCliSock.close()
