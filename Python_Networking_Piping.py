# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# Piping output of your program to tools like head(1) will cause a 
# SIGPIPE signal to be sent to your process when the receiver of its 
# standard output closes early. 
# This results in an exception like BrokenPipeError: [Errno 32] Broken pipe. 
# To handle this case, wrap your entry point to catch this exception as follows:
 

import os
import sys

def main():

    try:

        # simulate large output (your code replaces this loop)

        for x in range(10000):
            print("y")

        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.

        sys.stdout.flush()

    except BrokenPipeError:

        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown

        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE

if __name__ == '__main__':
    main()
