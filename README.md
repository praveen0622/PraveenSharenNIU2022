# PraveenSharenNIU2022
Following are the server and client codes for collabrative control on pioneer 3-DX robot using socketing and threading with python.
The Server will be the pioneer P3-DX robot and the client will be control PC.
The Server IP ADRESS = '192.168.1.31' and PORT = 7272


Server codes description
1. singleclientserver.py - It shows basic use of socketing to connect a server and client
2. singledataserver.py - The connection is followed by a data sent from client to server 
3. multiserver.py - The sockets has been established for multiple clients and connected to the server
4. singlemotionserver.py - The code gets the motion command from a single client and server implements the same.
5. singlecamserver.py - The server send web cam live stream to a single client
6. singleintserver.py - The simultaneous implementation of motion control and web cam stream has been done
6. multimotionserver.py - The motion commands are sent by multiple clients to the robot 
7. multiserver.py - The motion commands and web cam stream has been integrated for multiple clients
8. pmotionserver.py - The motion control has been coded with multiple option to vary the control ratios between multiple clients from 0 to 1.

Client codes description 

1. singleclientclient.py - It shows basic use of socketing to connect a server and client
2. singledataclient.py - The connection is followed by a data sent from client to server 
3. multiclient.py - The sockets has been established for multiple clients and connected to the server
4. singlemotionclient.py - The code gets the motion command from a single client and server implements the same.
5. singlecamclient.py - The server send web cam live stream to a single client
6. singleintclient.py - The simultaneous implementation of motion control and web cam stream has been done
6. multimotionclient.py - The motion commands are sent by multiple clients to the robot 
7. multiclient.py - The motion commands and web cam stream has been integrated for multiple clients
8. pmotionclient.py - The motion control has been coded with multiple option to vary the control ratios between multiple clients from 0 to 1.
