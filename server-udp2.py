#implementing server - udp after reading chapter2

import sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

s.bind(('127.0.0.1',PORT))
print ("Listening at ", s.getsockname())
while True:
	data, address = s.recvfrom(MAX)
	print ("The client at "+ str(address)+ " says " + (data).decode())
	mesg =  "Your data was " + str(len(data.decode())) + " bytes"
	s.sendto(mesg.encode() , address)