# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# asyncore Example basic echo server
# A basic echo server that uses the dispatcher class to accept connections 
# and dispatches the incoming connections to a handler:

import asyncore

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)

        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):

        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):

        print('Incoming connection from %s' % repr(addr))

        handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)

asyncore.loop()
