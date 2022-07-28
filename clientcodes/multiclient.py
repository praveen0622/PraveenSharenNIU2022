import socket
import sys

x = socket.socket()
port, host = 7272,'192.168.1.31'
x.connect((host,port))



