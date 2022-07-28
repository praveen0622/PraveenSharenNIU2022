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

from __future__ import division # For correct float division in Python 2
from AriaPy import *
import sys
import socket 
import threading 


class Main:

	
	def recv_from_client(self,con,addr):
		global command,g		
		command='50'
		#print("receving started")
		while(command!='27'):
			self.motion_from_client(command)			
			command=con.recv(1024)
			#print("Command is",command.decode())	
		
		print("MOTION CONTROL OFF")
		command='27'
		con.sendto(command.encode('utf-8'), (host,port))
		con.close()		
		return

	def motion_from_client(self,k):		
		temp = 0
		# Drive the robot a bit, then exit.

		if(k=='65'):
			robot.move(20)
			#print("Incremented speed")d
			k='0'
		if(k=='66'):
			robot.move(-20)
			#print("Decremented speed")
			k='0'
		if(k=='68'):
			robot.setDeltaHeading(15)
			#print("Incremented Rotational Speed")
			k='0'
		if(k=='67'):			
			robot.setDeltaHeading(-15)
			#print("Decremented Rotational Speed")
			k='0'
		if(k=='27'):
			print("MOTION STOPPED")	
			return False
		if(k=='0'):
			ArUtil_sleep(1)
		#print(k)
		return 

x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.31'
kdAct=0
x.bind((host,port))
print("WATITNG FOR CLIENT TO CONNECT")
print("CONNECT TO SERVER: ADDRESS:192.168.1.31, PORT:7272")
x.listen(3)
con,addr = x.accept()
print("CLIENT CONNECTED", addr)

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
object = Main()
print("MOTION CONTROL ON")
object.recv_from_client(con,addr)

del object
	
# Global library initialization, just like the C++ API:
x.close()
Aria_exit(1)
Aria_shutdown()
print("Exiting.")



