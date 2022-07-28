
from __future__ import division # For correct float division in Python 2
import sys
import socket 
import threading


from pynput import keyboard

class MyException(Exception): pass

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.31'
client.connect((host, port))
# define constants :
KEY_UP = 65
KEY_DOWN = 66
KEY_RIGHT = 67
KEY_LEFT = 68
KEY_ESC = 27
keyPress = 0

print ("Waiting for key press \n")	
print ("W,A,S,D = move robot \n")
print ("T = terminate \n")

def on_press(key):
	if (key == keyboard.Key.up):
		command=str(KEY_UP)
		client.sendto(command.encode('utf-8'), (host, port))
		print("Increment linear speed\n")
	elif (key == keyboard.Key.down):
		command=str(KEY_DOWN)
		client.sendto(command.encode('utf-8'), (host, port))
		print("Decrement linear speed\n")
	elif (key == keyboard.Key.left):
		command=str(KEY_LEFT)
		client.sendto(command.encode('utf-8'), (host, port))
		print("Increment rotational speed\n")
	elif (key == keyboard.Key.esc):
		command=str(KEY_ESC)
		client.sendto(command.encode('utf-8'), (host, port))
		return False
	elif (key == keyboard.Key.right):
		command=str(KEY_RIGHT)
		client.sendto(command.encode('utf-8'), (host, port))
		print("Decrement rotational speed\n")


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))

print("motion stopped")
command=client.recv(1024)
client.close()


