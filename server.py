#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print ('Server: Got connection from', socket.gethostname())
    c.send(('Connected to '+host+'.').encode())
    msg = c.recv(4096).decode();
    print ('Server: '+msg)
    s.close
