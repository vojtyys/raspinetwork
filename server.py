#!/usr/bin/python3
# raspinetwork (C) 2017 Vojtech Pail https://github.com/vojtyys/raspinetwork/blob/master/LICENSE

import socket
import threading

class serverThread(threading.Thread):
    def __init__(self, ID, client, addr):
        threading.Thread.__init__(self)
        self.ID = ID
        self.client = client
        self.addr = addr

    def run(self):
        print('Server: Got connection from: ',self.addr)
        self.client.send(("You are connected to:" + socket.gethostname() + '.').encode())
        msg = self.client.recv(4096).decode()
        print('Server: Msg from client ', self.addr, ': ', msg, '.')
        self.client.send(msg.encode())
        self.client.close()
        
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host, port))
s.listen(5)
th = []
index = 0
while True:
    c, addr = s.accept()
    t = serverThread(index, c, addr)
    t.run()
    th.append(t)
s.close()
