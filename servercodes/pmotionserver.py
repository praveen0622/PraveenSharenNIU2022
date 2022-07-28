import socket
import os
import thread
import threading
ServerSideSocket = socket.socket()
host = '192.168.1.31'
port = 7272
ThreadCount = 0

"""
Adept MobileRobots Robotics Interface for Applications (ARIA)
Copyright (C) 2004-2005 ActivMedia Robotics LLC
Copyright (C) 2006-2010 MobileRobots Inc.
Copyright (C) 2011-2015 Adept Technology, Inc.
Copyright (C) 2016 Omron Adept Technologies, Inc.

     This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with this program; if not, write to the Free Software
     Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

If you wish to redistribute ARIA under different terms, contact 
Adept MobileRobots for information about a commercial version of ARIA at 
robots@mobilerobots.com or 
Adept MobileRobots, 10 Columbia Drive, Amherst, NH 03031; +1-603-881-7960
"""
 # For correct float division in Python 2
from AriaPy import *
import sys
import socket 
from threading import * 
import threading 
import cv2
import pickle
import struct ## new
import imutils
from time import sleep
from pickle import dumps


def recv_from_client(client_socket,addr,th,control):
	global command
	command='50'
	print("MOTION CONTROL IS ON")			
	print("receving started")
	if(th==1):
		t3 = threading.Thread(target=video_to_client,args=(client_socket,addr,command))
		t3.start()
		print("thread 3 created")
	if(th==2):
		t4 = threading.Thread(target=video_to_client,args=(client_socket,addr,command))
		t4.start()
		print("thread 4 created")
	while(command!='27'):
		if(th==1):
			command=client_socket.recv(1024)
			if(control==1):
				motion_from_client(command,1,control,1)
			if(control==2):
				motion_from_client(command,1,control,0)
			if(control==3):
				motion_from_client(command,1,control,0.25)
			if(control==4):
				motion_from_client(command,1,control,0.75)	
		if(th==2):
			command=client_socket.recv(1024)
			if(control==1):
				motion_from_client(command,2,control,0)
			if(control==2):
				motion_from_client(command,2,control,1)			
			if(control==3):
				motion_from_client(command,2,control,0.75)
			if(control==4):
				motion_from_client(command,2,control,0.25)
			
	print("MOTION CONTROL OFF")
	video_to_client(client_socket,addr,command)
	client_socket.close()		

		
def motion_from_client(k,user,se,weight):				
	# Drive the robot a bit, then exit.
	print("user is",user," and setting is", se)
	if(k=='65'):
		robot.move(100*weight)
		print("Incremented speed")
		k='0'
	if(k=='66'):
		robot.move(-100*weight)
		print("Decremented speed")
		k='0'
	if(k=='68'):
		robot.setDeltaHeading(15*weight)
		print("Incremented Rotational Speed")
		k='0'
	if(k=='67'):			
		robot.setDeltaHeading(-15*weight)
		print("Decremented Rotational Speed")
		k='0'
	if(k=='27'):
		print("MOTION STOPPED")	
	if(k=='0'):
		ArUtil_sleep(1)
		#print(k)
		
	
	
	
def video_to_client(client_socket,addr,key):
	print("VIDEO STREAM IS ON")
	while True:
		print('GOT CONNECTION FROM:',addr)
		if client_socket:
			vid = cv2.VideoCapture(0)
			while(vid.isOpened()):
				img,frame = vid.read()
				frame = imutils.resize(frame,width=180)
				a = pickle.dumps(frame, 0)
				message = struct.pack("Q",len(a))+a
				client_socket.sendall(message)
				#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				cv2.imshow('TRANSMITTING VIDEO',frame)
				key = cv2.waitKey(1) & 0xFF
				if key  == '27':
					#cv2.destroyAllWindows()
					break


x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.31'
kdAct=0
x.bind((host,port))
print("WATITNG FOR CLIENT TO CONNECT")
print("CONNECT TO SERVER: ADDRESS:192.168.1.31, PORT:7272")

Aria_init()
	
parser = ArArgumentParser(sys.argv)
parser.loadDefaultArguments()
	
# Create a robot object:
robot = ArRobot()
		

# Create a "simple connector" object and connect to either the simulator
# or the robot. Unlike the C++ API which takes int and char* pointers, 
# the Python constructor just takes argv as a list.
print("Connecting...")
conn = ArRobotConnector(parser, robot)
if not Aria_parseArgs():
	Aria_logOptions()
	Aria_exit(1)

if not conn.connectRobot():
	print("Could not connect to robot, exiting")
	Aria_exit(1)

# Run the robot threads in the background:
print("Running...")
robot.runAsync(1)
robot.enableMotors()
robot.setHeading(0)

print("Enter the MODE")
print("Enter 1.FULL C1 2.FULL C2 3.PAR C1 4.PAR C2")
ct=input()
print("MODE HAS BEEN SET")
x.listen(2)
global client_socket,addr

global threadcount 
threadcount = 0
global count 
count = 0
while True:
	client_socket, addr = x.accept()
	print('Connected to: ' + addr[0] + ':' + str(addr[1]))
	threadcount += 1
	if(threadcount==1 and count==0):
		t1 = threading.Thread(target=recv_from_client,args=(client_socket,addr,threadcount,ct))
		t1.start()
		count+=1
		print("Thread 1 created")
		print("Thread count is",threadcount)
	if(threadcount==2):
		t2 = threading.Thread(target=recv_from_client,args=(client_socket,addr,threadcount,ct))
		t2.start()
		print("Thread 2 created")
		break
	

# Global library initialization, just like the C++ API:
t1.join()
t2.join()
x.close()
Aria_exit(1)
Aria_shutdown()
print("Exiting.")



