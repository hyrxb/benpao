#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import socket

BUF_SIZE = 1024

server_addr = ('127.0.0.1',8888)

try:
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
	print "Creating Socket Failure .Error Code: " + str(msg[0]) + "Messgae:" + msg[1]
	sys.exit()

client.connect(server_addr)
while True:
	data = raw_input("Please input some string > ")
	if not data:
		print "input can't empty,Please input again.."
		continue
	client.sendall(data)
	data = client.recv(BUF_SIZE)
	print data
client.close()
