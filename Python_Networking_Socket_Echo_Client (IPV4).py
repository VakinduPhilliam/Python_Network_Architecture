# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.

# Echo client program

import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')

    data = s.recv(1024)

print('Received', repr(data))
