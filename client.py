#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = '89.177.139.187'

s.connect((host, port))
print (s.recv(4096))
msg = raw_input('Enter a message:')
s.send(msg)
s.close()
