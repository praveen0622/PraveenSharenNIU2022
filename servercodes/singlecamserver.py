#from IPython.display import clear_output
import sys
import socket 
import threading 
import cv2
import pickle
import struct ## new
import imutils
from pickle import dumps

#SERVER SOCKET
x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port,host=7272,'192.168.1.31'

x.bind((host,port))

print("WATITNG FOR CLIENT TO CONNECT")
print("CONNECT TO SERVER: ADDRESS:192.168.1.31, PORT:7272")
x.listen(3)

while True:
	client_socket,addr = x.accept()
	print('GOT CONNECTION FROM:',addr)
	if client_socket:
		vid = cv2.VideoCapture(0)
		
		while(vid.isOpened()):
			img,frame = vid.read()
			frame = imutils.resize(frame,width=320)
			a = pickle.dumps(frame, 0)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			
			cv2.imshow('TRANSMITTING VIDEO',frame)
			key = cv2.waitKey(1) & 0xFF
			if key  == ord('q'):
        			break




print("STREAMING STOPPED")




