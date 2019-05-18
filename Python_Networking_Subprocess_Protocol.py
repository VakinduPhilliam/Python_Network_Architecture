# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# loop.subprocess_exec() and SubprocessProtocol
# An example of a subprocess protocol used to get the output of a subprocess 
# and to wait for the subprocess exit.
# The subprocess is created by th loop.subprocess_exec() method:
 
import asyncio
import sys

class DateProtocol(asyncio.SubprocessProtocol):

    def __init__(self, exit_future):
        self.exit_future = exit_future
        self.output = bytearray()

    def pipe_data_received(self, fd, data):
        self.output.extend(data)

    def process_exited(self):
        self.exit_future.set_result(True)

async def get_date():

    # Get a reference to the event loop as we plan to use
    # low-level APIs.

    loop = asyncio.get_running_loop()

    code = 'import datetime; print(datetime.datetime.now())'
    exit_future = asyncio.Future(loop=loop)

    # Create the subprocess controlled by DateProtocol;
    # redirect the standard output into a pipe.

    transport, protocol = await loop.subprocess_exec(
        lambda: DateProtocol(exit_future),
        sys.executable, '-c', code,
        stdin=None, stderr=None)

    # Wait for the subprocess exit using the process_exited()
    # method of the protocol.

    await exit_future

    # Close the stdout pipe.

    transport.close()

    # Read the output which was collected by the
    # pipe_data_received() method of the protocol.

    data = bytes(protocol.output)
    return data.decode('ascii').rstrip()

if sys.platform == "win32":
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy())

date = asyncio.run(get_date())

print(f"Current date: {date}")
