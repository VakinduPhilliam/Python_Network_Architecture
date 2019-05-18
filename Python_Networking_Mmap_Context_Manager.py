# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# mmap can also be used as a context manager in a 'with' statement:
 
import mmap

with mmap.mmap(-1, 13) as mm:
    mm.write(b"Hello world!")
