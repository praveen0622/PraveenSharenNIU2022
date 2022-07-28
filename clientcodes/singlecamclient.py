import cv2
import socket
import struct
import pickle
import socket,cv2, pickle,struct


#CLIENT SOCKET



client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.31'
client_socket.connect((host,port)) # a tuple
data = b""
payload_size = struct.calcsize("Q")
while True:
	while len(data) < payload_size:
		packet = client_socket.recv(4*1024) # 4K
		if not packet: break
		data+=packet
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q", packed_msg_size)[0]
	
	while len(data) < msg_size:
		data += client_socket.recv(4*1024)
	frame_data = data[:msg_size]
	data  = data[msg_size:]
	frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
	cv2.imshow("RECEIVING VIDEO",frame)
	key = cv2.waitKey(1) & 0xFF
	if cv2.waitKey(1) == ord('q'):
		break
client_socket.close()


