#!/usr/bin/python3

import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket() # instantiate
    client_socket.connect((host, port)) # connect to the server

    message = input (" -> ") # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data) # show data in terminal

        message = input(" -> ") # Accept more input

    client_socket.close() #close the connection