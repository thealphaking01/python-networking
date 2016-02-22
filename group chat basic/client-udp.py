#client of chat application python3
import sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

while True:
	a = input()
	if a:
		s.sendto(a.encode(),('127.0.0.1', PORT))    