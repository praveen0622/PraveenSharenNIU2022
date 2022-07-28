import sys
import socket


#Creating a INTET and Streaming socket with TCP Protocol
#The port number is defined for the P3-DX as 7272
#The host IP address will be the server address to which client will be connected and in this case IP of P3-DX

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.31'

#Command to connect with server using IP AND PORT
client_socket.connect((host, port))

# Sending Data to server
data = "Hello Server!";
client_socket.send(data.encode());


# Receive message from server
message = client_socket.recv(1024);

print(message.decode());

