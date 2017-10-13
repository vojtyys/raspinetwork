#!/usr/bin/python3

import socket
import threading

class serverThread(threading.Thread):
    def __init__(self, ID, client, addr):
        threading.Thread.__init__(self)
        self.ID = ID
        self.client = client
        self.addr = addr

    def run(self):
        print('Server: Got connection from: ', addr)
        client.send(("You are connected to:" + socket.gethostname() + '.').encode())
        print('Server: Msg from client ' + addr + ': ' + client.recv(4096).decode() + '.')
        
        
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host, port))
s.listen(5)
threads = []
index = 0
while True:
    c, addr = s.accept()
    t = serverThread(index, c, addr)
    s.close()
   
