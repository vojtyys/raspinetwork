#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print ('Server: Got connection from', addr)
    c.send(('Connected to '+socket.gethostname()+'.').encode())
    msg = c.recv(4096).decode();
    print ('Server: '+msg)
    c.send(msg.encode())
    s.close
    print('Server: Connection to ', addr, ' has been closed.')
