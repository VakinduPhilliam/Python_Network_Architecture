# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# The socketserver module simplifies the task of writing network servers.
# Client side:
 
import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Connect to server and send data

    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down

    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
