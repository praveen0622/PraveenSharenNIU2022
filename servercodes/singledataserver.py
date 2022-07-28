import sys
import socket

#Creating a INTET and Streaming socket with TCP Protocol
#The port number is defined for the P3-DX as 7272
#The host IP address will be the server address and in this case IP of P3-DX
x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.31'

#Bind helps the incoming connenction to enter host through a specfic binded port
x.bind((host,port))
print("WATITNG FOR CLIENT TO CONNECT")
print("CONNECT TO SERVER: ADDRESS:192.168.1.31, PORT:7272")

#the server waits for connection for number of clients as specified 
x.listen(3)
#note listen is blocking command 

#the server accepts the client connection using client_socket as the object
#addr stores the client address 
client_socket,addr = x.accept()
print("CLIENT CONNECTED", addr)

#Receiving an printing message from client
message = client_socket.recv(1024)
print(message.decode());
 

# Sending data back to the client
client_socket.send("Hello Client!".encode());





