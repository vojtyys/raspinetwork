#!/usr/bin/python3

import socket

s = socket.socket(AF_INET,SOCK_STREAM)
port = 12345
host = '89.177.139.187'

s.connect((host, port))
print s.recv(4096)
s.send(msg)
s.close()
