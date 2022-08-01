# PraveenSharenNIU2022
Following are the server and client codes for collabrative control on pioneer 3-DX robot using socketing and threading with python.
The Server will be the pioneer P3-DX robot and the client will be control PC.
The Server IP ADRESS = '192.168.1.31' and PORT = 7272


Server codes description
1. singleclientserver.py 
    It shows basic use of socketing to connect a server and client (starts from bind->listen->accept)

2. singledataserver.py 
    The connection is followed by a data sent from client to server ( using .recv and .send )
    
3. multiserver.py 
    The sockets has been established for multiple clients and connected to the server (by using a while loop and       append command.
    
4. singlemotionserver.py  
    The code gets the motion command from a single client and server implements the same (the ascii code of the         keystroke is sent through socketing and motion is exceuted using the ros commands).
    
5. singlecamserver.py  
    The server send web cam live stream to a single client (by using CV2 and converting the video into pixel stream     and sent to client using sendall command)
    
6. singleintserver.py  
    The simultaneous implementation of motion control and web cam stream has been done (threading is used to run       the stream seprately while we wait for the keystrokes from client side)

6. multimotionserver.py 
    The motion commands are sent by multiple clients to the robot (A unique thread is created for each client           connected for the motion control)

7. multiintserver.py 
    The motion commands and web cam stream has been integrated for multiple clients
    (multiple threading is used for each client connected to exceute both stream and motion control).
    
8. pmotionserver.py 
    The motion control has been coded with multiple option to vary the control ratios between multiple clients from     0 to 1. (the key idea is to vary the amount motion power we give to each client which is varied according to       the ratio required).

Client codes description 

1. singleclientclient.py 
    It shows basic use of socketing to connect a server and client (using connect).
    
2. singledataclient.py 
    The connection is followed by a data sent from client to server (using .send and the socket object).
    
3. multiclient.py 
    The sockets has been established for multiple clients and connected to the server (multiple laptops were used).

4. singlemotionclient.py 
    The code sends the motion command to the server. (the keyboard and keypress function has been used to read the     keystrokes and there respective ascii codes have been sent to the server through sockets).
    
5. singlecamclient.py 
    The client recevies the live stream from a the server (the pixel packets are decoed to display the video stream     using CV2).
    
6. singleintclient.py 
    The simultaneous implementation of motion control and web cam stream has been done (similar to server part         muliple threads have been used for the stream and motion control).
    
6. multimotionclient.py 
    The motion commands are sent by multiple clients to the robot (same code from multiple clients)
    
7. multiclient.py 
    The motion commands and web cam stream has been integrated for multiple clients
    (similar to server multiple unique thread for eac client has been used)
8. pmotionclient.py
    The motion control has been coded with multiple option to vary the control ratios between multiple clients from     0 to 1. (no change in client code same as normal intergrated motion and stream control).
