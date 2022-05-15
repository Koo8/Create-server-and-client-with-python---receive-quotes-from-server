'''
    This is the server, wait for receiving requests from clients
'''
import socket
import random

quote_db = [
    '''The greatest glory in living lies not in never falling, 
    but in rising every time we fall. -Nelson Mandel''', 
    '''The way to get started is to quit talking and begin 
    doing. -Walt Disney''',
    '''Your time is limited, so don't waste it living someone 
    else's life. Don't be trapped by dogma – which is living 
    with the results of other people's thinking. -Steve Jobs''',
    '''If life were predictable it would cease to be life, and 
    be without flavor. -Eleanor Roosevelt''',
    '''If you look at what you have in life, you'll always have 
    more. If you look at what you don't have in life, you'll 
    never have enough. -Oprah Winfrey'''
]


# use this local computer as the server, 
# cmd->ipconfig->ipv4 address can also mannually get the address
host = socket.gethostbyname(socket.gethostname())
# use a port number outside the 'well-known's
port = 8989

# create a socket for connecting to clients, 
# not for talking to clients. 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp
# bind to a tuple
socket.bind((host, port))
# queue up max 5 connect requests b4 refusing outside connections.
socket.listen(5)

# run server infitely
while True:
    # wait and accept requests from clients, a new socket is created
    # for talking to this client with the ip address
    (newlycreatedsocketforclient, clientIPaddress) = socket.accept()
    # receive message from client
    msg = newlycreatedsocketforclient.recv(1024) # bytes
    # decode msg for human
    decoded_msg = msg.decode('utf-8')
    print(decoded_msg)
    # to send message to the client, use encode() 
    index = random.randint(0, 4)
    print(index)
    quote_to_send = quote_db[index]
    newlycreatedsocketforclient.send(f"Thank you! Your quote today is: {quote_to_send}".encode())

    # server can be closed if needed
    # newlycreatedsocketforclient.close()

