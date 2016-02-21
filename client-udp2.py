#implementing client - udp after reading chapter2

import sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

print ("Address before sending" + str(s.getsockname()))
s.sendto("This is my message".encode(), ('127.0.0.1', PORT))
print ("Address after sending" + str(s.getsockname()))
data, address = s.recvfrom(MAX)
print (repr(data))
exit()