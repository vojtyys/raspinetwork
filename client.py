#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = '89.177.139.187' 

s.connect((host, port))
print ('Client: connection has been established')
print ('Client: '+s.recv(4096).decode()) 
msg = input('Client: Enter a message: ')
s.send(msg.encode())
print(s.recv(4096).decode())
s.close()
print ('Client: connection to server has been closed.')
