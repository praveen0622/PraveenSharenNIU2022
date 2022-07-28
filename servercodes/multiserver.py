import socket
import threading
from pickle import dumps, loads

x=socket.socket()
port, host = 7272,'192.168.1.31'
x.bind((host,port))
print("WATITNG FOR CLIENT TO CONNECT")
print("CONNECT TO SERVER: ADDRESS:192.168.1.31, PORT:7272")

#2 represents the maximum number of clients which can be connected
x.listen(2)
clients=[]

i=0
while i<2:
	con, addr = x.accept()
	clients.append((con,addr))
	print("Client Connected", addr)
	i+=1


 

_
