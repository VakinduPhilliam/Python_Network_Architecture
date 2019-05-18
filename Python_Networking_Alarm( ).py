# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# This example uses the alarm() function to limit the time spent waiting 
# to open a file; this is useful if the file is for a serial device that 
# may not be turned on, which would normally cause the os.open() to hang indefinitely. 
# The solution is to set a 5-second alarm before opening the file; if the operation 
# takes too long, the alarm signal will be sent, and the handler raises an exception.
 
import signal, os

def handler(signum, frame):

    print('Signal handler called with signal', signum)

    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely

fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm
