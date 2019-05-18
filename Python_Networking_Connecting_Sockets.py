# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# Connecting Existing Sockets
# Wait until a socket receives data using the loop.create_connection() method with a protocol:
 
import asyncio
import socket

class MyProtocol(asyncio.Protocol):

    def __init__(self, loop):
        self.transport = None
        self.on_con_lost = loop.create_future()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print("Received:", data.decode())

        # We are done: close the transport;
        # connection_lost() will be called automatically.
        self.transport.close()

    def connection_lost(self, exc):

        # The socket has been closed

        self.on_con_lost.set_result(True)


async def main():

    # Get a reference to the event loop as we plan to use
    # low-level APIs.

    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets

    rsock, wsock = socket.socketpair()

    # Register the socket to wait for data.

    transport, protocol = await loop.create_connection(
        lambda: MyProtocol(loop), sock=rsock)

    # Simulate the reception of data from the network.

    loop.call_soon(wsock.send, 'abc'.encode())

    try:
        await protocol.on_con_lost

    finally:
        transport.close()
        wsock.close()

asyncio.run(main())
