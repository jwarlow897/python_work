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
	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*/)
	else:
		raise EnvironmentError('Unsupported platform')
		
	reult = []
	for port in ports:
		try:
			s. = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	return result
	
if __name__ == '__main__':
	print(serial_ports())