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

# Echo client program

import socket
import sys

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res

    try:
        s = socket.socket(af, socktype, proto)

    except OSError as msg:
        s = None
        continue

    try:
        s.connect(sa)

    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:

    print('could not open socket')
    sys.exit(1)

with s:

    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
