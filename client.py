''' This is the client, send out request to a server '''

import socket


# the server is the current computer
server_host = socket.gethostbyname(socket.gethostname())
# port number has to be the same as the server
port = 8989

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# use a tuple
socket.connect((server_host, port))
# for sending requests to server
socket.send(f'Good Day! from a host client.'.encode())
# for receiving response from server
message = socket.recv(1024)
print(message)
