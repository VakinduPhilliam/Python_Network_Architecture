# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# This example shows how to write a very simple network sniffer with 
# raw sockets on Windows. 
# The example requires administrator privileges to modify the interface:
 
import socket

# the public network interface

HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package

print(s.recvfrom(65565))

# disabled promiscuous mode

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
