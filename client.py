#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = '89.177.139.187' 

s.connect((host, port))
print ('client: connected')
print ('client: '+s.recv(4096).decode()) 
msg = input('Client: Enter a message: ')
s.send(msg.encode())
s.close()
