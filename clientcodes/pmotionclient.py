from __future__ import division  # For correct float division in Python 2
import sys
import threading
import socket
from threading import *
import cv2, pickle, struct
#the socketing part with robot IP and PORT
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7272
host = '192.168.1.31'
client_socket.connect((host, port))

#the function for web cam streaming 
def video_from_server():
    print("video stream started")
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(2 * 1024)  # 4K
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
	#the video is converted to a pixel stream and sent through the socket
        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        cv2.imshow("RECEIVING VIDEO", frame)
	#cv2 (computer vision) to extract the video from web cam
        key = cv2.waitKey(1) & 0xFF
        if key == keyboard.Key.esc:
            cv2.destroyAllWindows()
            break
    print("video stream ended")
#thread is created for te web cam streaming process
t1 = threading.Thread(target=video_from_server)
t1.start()
#this ensures the code can wait for key input and also stream the video in seprate thread
from pynput import keyboard

# define constants :
KEY_UP = 65
KEY_DOWN = 66
KEY_RIGHT = 67
KEY_LEFT = 68
KEY_ESC = 27
key = 0
keyPress = 0
print("Waiting for key press \n")
print("W,A,S,D = move robot \n")
print("Esc = terminate \n")

#function definition for key stroke input 
class MyException(Exception): pass
#the function is automatically called when a key is pressed 
def on_press(key):
	if (key == keyboard.Key.up):
		command=str(KEY_UP)
		client_socket.sendto(command.encode('utf-8'), (host, port))
		print("Increment linear speed\n")
	elif (key == keyboard.Key.down):
		command=str(KEY_DOWN)
		client_socket.sendto(command.encode('utf-8'), (host, port))
		print("Decrement linear speed\n")
	elif (key == keyboard.Key.left):
		command=str(KEY_LEFT)
		client_socket.sendto(command.encode('utf-8'), (host, port))
		print("Increment rotational speed\n")
	elif (key == keyboard.Key.esc):
		command=str(KEY_ESC)
		client_socket.sendto(command.encode('utf-8'), (host, port))
		return False
	elif (key == keyboard.Key.right):
		command=str(KEY_RIGHT)
		client_socket.sendto(command.encode('utf-8'), (host, port))
		print("Decrement rotational speed\n")

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
print("thread started")
print("motion stopped and video stream stopped")
client_socket.close()
