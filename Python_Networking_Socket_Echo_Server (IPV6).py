# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# The server side will listen to the first address family available 
#v (it should listen to both instead). On most of IPv6-ready systems, 
# IPv6 will take precedence and the server may not accept IPv4 traffic. 
# The client side will try to connect to the all addresses returned as 
# a result of the name resolution, and sends traffic to the first one 
# connected successfully.
 
# Echo server program

import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res

    try:
        s = socket.socket(af, socktype, proto)

    except OSError as msg:
        s = None
        continue

    try:
        s.bind(sa)
        s.listen(1)

    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:

    print('could not open socket')

    sys.exit(1)
conn, addr = s.accept()

with conn:
    print('Connected by', addr)

    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
