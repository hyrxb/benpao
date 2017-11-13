from socket import *
from time import ctime

print("===============================")

HOST = ''
PORT = 21567
BUFSIZ  =1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("ddd")
    tcp,addr = tcpSerSock.accept()
    print('取得链接：',addr)

    while True:
        data = tcp.recv(BUFSIZ)
        if not data:
            break
        tcp.send(data)
    tcp.close()
tcpSerSock.close()