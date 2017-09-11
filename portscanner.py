# First wireless port scanner
# !/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear',shell=True)

# Request input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print out information on which host we are about to scan

print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Use range function to specify ports (here it scans all ports between 1 and 1024)

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print ("Port{}: Open", format(port))
		sock.close()
		
except KeyboardInterrupt:
	print ("You pressed Ctrl+C")
	sys.exit()
	
except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()
	
except socket.error:
	print ("Couldn't connect to server")
	sys.exit()

# Get next datetime and use difference to see how long script ran
	
t2 = datetime.now()
total = t2-t1

print ('Scanning Completed in: ' . total)
