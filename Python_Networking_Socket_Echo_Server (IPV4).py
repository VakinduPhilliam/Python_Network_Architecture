# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# An example programs using the TCP/IP protocol: a server that echoes all 
# data that it receives back (servicing only one client), and a client using it. 
# Note that a server must perform the sequence socket(), bind(), listen(), 
# accept() (possibly repeating the accept() to service more than one client), 
# while a client only needs the sequence socket(), connect(). 
# Also note that the server does not sendall()/recv() on the socket it is 
# listening on but on the new socket returned by accept().

# Echo server program

import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()

    with conn:

        print('Connected by', addr)

        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
