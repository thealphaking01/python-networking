#server for chat application python3

import sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

s.bind(('127.0.0.1',PORT))
print ("Listening at ", s.getsockname())
all_users = {}
while True:
	data, address = s.recvfrom(MAX)
	if address not in all_users.keys():
		for i in all_users.keys():
			mesg = " New user joined : " + str(address)
		all_users[address]=1
	print ("User " + str(address) + " : " + str((data).decode()))
	