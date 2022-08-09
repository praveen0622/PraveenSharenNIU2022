# PraveenSharenNIU2022
Following is the description of the codes for multi client partial control on pioneer 3-DX robot using socketing and threading with python.
The Server will be the pioneer P3-DX robot and the client will be control PC.
The Server IP ADDRESS = '192.168.1.31' and PORT = 7272

#Equipment 
- Pioneer 3-DX Robot 
- Laptops (min 2) installed with python version > 2.0
- Webcam
- Robot power cable, display monitor, keyboard and mouse

#Software 
- Windows 10 
- Pycharm > 2021.1.3 
- Python > 2.7.12

#Setting up the PIONEER 3-DX Robot 
1. Connect the power cable, keyboard, mouse and webcam to the pioneer 3-DX robot 
2. connect the HDMI cable of the display to the robot 
3. TURN ON the robot power with the physical key with label on and off (LEFT SIDE OF THE ROBOT) 
4. TURN ON the on-board computer with the physical key with the label power (RIGHT SIDE OF THE ROBOT)
5. USE THE LOGIN PASSWORD: mobile2591  
 ##Running the server side code:
1. Open the terminal 
2. Set directory to  pythonExamples folder (type: cd /usr/local/Aria/PythonExamples ) 
3. Run the server code pmotionserver (type: python pmotionserver.py )
4. Set up the mode you want to run the motion control (type 1-5 for the respective mode) 
5. Wait for the client side to connect 
6. After the clients are connected all set to MOTION CONTROL using keys from client 


#Setting up client side 
1.Open command prompt 
2. Set directory to the folder containing the pmotionclient code (type: cd to change directory) 
3. Run the client code pmotionclient (type: python pmotionclient.py) 
4. Wait for both the clients to connect 
5. The web cam feed will be displayed on the monitor 
6. Enter arrow keys to control the motion and ESC key to terminate 


CODE DESCRIPTION: This contains the description of server and client codes including the main and all functions in the code.
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
2. Use predefined casesenstive motion commands to control the robot and assign the control variable back to zero 
    2.1 robot.move to increment and decrement linear speed 
    2.2 robot.setDeltaHeading to increment and decrement rotational speed 
    2.3 use a dummy loop to make sure the robot sleeps when no command is received  
3. To make the robot sleep use ArUtil_sleep() 

#video_to_client 
1. Use cv2.Videocapture(0) to use the connected webcam to capture a video ( 0 -Primary Camera , 1-Secondary Camera) 
2. Create a while lopp which exceutes when the webcam is on using vid.isOpened() 
3. Read the video usind 2 variables to store the video as pixel stream 
4. Using imutils to resize the video frame to a width
5. pack the pixel data to a varaible using dumps
6. send the pixel stream to the client using .sendall with the socket object 
7. cv2.imshow to display the video stream on the robot monitor 
8. use when cv2.destroyAllWindows to close the stream    


#CLIENT CODE 
#MAIN FUNCTION 
1. open pycharm or any python wrapper and create a new file with .py extension 
2. Import the required header files - (sys, threading, socket, cv2, pickle, struct)
3. Create a socket with tcp protocol and a object name 
4. Assign 2 variables host and port to store the IP and port of the server(Pioneer Robot)
5. Use .bind function to bind the host and port 
6. Create a thread to call the video_from_ server to stream the video seprately as the client waits for key inputs 
7. define constant variables and assign values for all the keystrokes and esc key 
    7.1 65-UP, 66-DOWN, 67-RIGHT, LEFT-68, ESC-27 
8. Create a class with function named on_press(key) (NOTE: on_press is pre defined function with pre defined variable key donot change the name)
9. the key variable stores the keystroke input in form of an ascii code. 
10. use if loops to compare the keystroke with the predefined constants to find the type of keystroke 
11. send the respective ascii code to the server using client socket object and .sendto command 
12. terimante on esc key by using return false statment
13. close the socket using objectname.close() 
