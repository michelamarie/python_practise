#!/usr/bin/python3

import socket

def server_program():
    # get the host name
    host = socket.gethostname()
    port = 5000 # initiate port number

    server_socket = socket.socket() #get instance
    server_socket.bind((host, port)) #bind address and port to application

    # Define number of allowed clients
    server_socket.listen(2)
    conn, address = server_socket.accept() # accept a new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream
        data = conn.recv(1024).decode()
        if not data:
            # if data  is not received, break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode()) # send data to the client

if __name__ == '__main__':
    server_program()