#to get the ip address of a host name
import socket
hostname = 'maps.google.com'
addr = socket.gethostbyname(hostname)
print ("The address of " +hostname+" is "+addr)