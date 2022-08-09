# PraveenSharenNIU2022
Following is the description of the codes for multi client partial control on pioneer 3-DX robot using socketing and threading with python.
The Server will be the pioneer P3-DX robot and the client will be control PC.
The Server IP ADRESS = '192.168.1.31' and PORT = 7272

#Equipment 
- Pioneer 3-DX Robot 
- Laptops (min 2) installed with python version > 2.0
- Webcam
- Robot power cable, display monitor, keyboard and mouse

#Software 
- Windows 10 
- Pycharm > 2021.1.3 
- Python > 2.7.12

#Server(Robot) Code

#MAIN FUNCTION 
1. Open gedit on Robot PC -> create a new file with .py extenstion
2. Import main header AriaPy   
3. Import the required header files - (system, cv2, struct, imutils, sleep from time, dumps from pickle, socket, os, thread, threading)
4. Create a socket with tcp protocol and a object name 
5. Assign 2 variables host and port to store the IP and port of the server(Pioneer Robot)
6. Use .bind function to bind the host and port 
7. Define Aria_init() to setup the ROS part to establish motion control 
8. Create a robot object 
9. Create a simple connector with ArRobotConnector()
10. Enable robot motors with .enableMotors (NOTE: the aria functions are casesenstive)
11. Define and assign the value to variable to get user input for what mode to be set up.
12. Use .listen function to wait for client to connect (NOTE: .listen is a blocking call so the code stops here and waits for connection) 
13. Define a While loop 
    13.1 Use .accept fucntion with 2 variables for storing client(user) address and a object.
    13.2 Create 2 threads (1 & 2)  with each thread calling the recv_from_client function using .thread and .start 
14. use .join to wait for the threads to complete the process 
15. Close Aria using Aria_exit and Aria_shutdown  

#recv_from_client function 
1. Define a global variable to store the ascii code(keystrokes) received from client 
2. Create 2 threads (3 & 4) to call the video_to_client to start web cam streaming to the user 
3. Define a while loop and if loop to assign the respective weights according to the mode requested by the user 
    3.1 1/0 (FULL CONTROL CLIENT 1) 
    3.2 0/1 (FULL CONTROL CLIENT 2)
    3.3 0.25/0/75 (PARTIAL CONTROL CLIENT 1)
    3.4 0.5/0.5 (EQUAL CONTROL FOR BOTH CLIENTS)
    3.5 0.75/0.25 (PARTIAL CONTROL CLIENT 2)
4. CALL the motion_from_client function with the assigned weights and a value (1 or 2) to understand which client sent the command 


#motion_from_client 
1. Use if loops to compare the ascii codes and determine what kind of keystroke is recived from the client through recv_from_client finction 
2. Use predefined casesenstive motion commands to control the robot 
    2.1 robot.move to increment and decrement linear speed 
    2.2 robot.setDeltaHeading to increment and decrement rotational speed  
#Setting up 
6. Download Python on both the laptops with the minimum version mentioned in the #Software 
7.  
Server codes description

1. singleclientserver.py -> It shows basic use of socketing to connect a server and client (starts from             bind->listen->accept)

2. singledataserver.py -> The connection is followed by a data sent from client to server ( using .recv and .send )
    
3. multiserver.py -> The sockets has been established for multiple clients and connected to the server (by using a  while loop and append command.
    
4. singlemotionserver.py -> The code gets the motion command from a single client and server implements the same   (the ascii code of the keystroke is sent through socketing and motion is exceuted using                             the ros commands).
    
5. singlecamserver.py -> The server send web cam live stream to a single client (by using CV2 and converting the video into pixel stream and sent to client using sendall command)
    
6. singleintserver.py -> The simultaneous implementation of motion control and web cam stream has been done (threading is used to run the stream seprately while we wait for the keystrokes from client side)

7. multimotionserver.py -> The motion commands are sent by multiple clients to the robot (A unique thread is created for each client connected for the motion control)

8. multiintserver.py -> The motion commands and web cam stream has been integrated for multiple clients
(multiple threading is used for each client connected to exceute both stream and motion control).
    
9. pmotionserver.py -> The motion control has been coded with multiple option to vary the control ratios between multiple clients from 0 to 1. (the key idea is to vary the amount motion power we give to each client which is varied according to the ratio required).

Client codes description 

1. singleclientclient.py -> It shows basic use of socketing to connect a server and client (using connect).
    
2. singledataclient.py -> The connection is followed by a data sent from client to server (using .send and the socket object).
    
3. multiclient.py -> The sockets has been established for multiple clients and connected to the server (multiple laptops were used).

4. singlemotionclient.py -> The code sends the motion command to the server. (the keyboard and keypress function has been used to read the keystrokes and there respective ascii codes have been sent to the server through sockets).
    
5. singlecamclient.py -> The client recevies the live stream from a the server (the pixel packets are decoed to display the video stream using CV2).
    
6. singleintclient.py -> The simultaneous implementation of motion control and web cam stream has been done (similar to server part muliple threads have been used for the stream and motion control).
    
7. multimotionclient.py -> The motion commands are sent by multiple clients to the robot (same code from multiple clients)
    
8. multiclient.py -> The motion commands and web cam stream has been integrated for multiple clients
(similar to server multiple unique thread for eac client has been used)

9. pmotionclient.py -> The motion control has been coded with multiple option to vary the control ratios between multiple clients from 0 to 1. (no change in client code same as normal intergrated motion and stream control).
