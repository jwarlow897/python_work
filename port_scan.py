import sys 
import glob
import serial

def serial_ports():
	"""Lists serial port names
https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
	"""

	

	if sys.platform.startswith('win'):
		ports = ['COM%s' % (i + 1) for i in range(256)]
	elif sys.platform.startswith('linux') or sys.platform.startwith('cygwin'):
	# apparently excludes "/dev/tty"
	ports = glob.glob('/dev/tty[A-Za-z]*')
