#!/usr/bin/env python3

import socket

UDP_IP = "::1"
# UDP_IP = "2a00:1450:400d:805::200e" # google.com
UDP_PORT = 5001
UDP_PORT = 5000
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

data, ip = sock.recvfrom(1024)

print("{}: {}".format(ip, data.decode()))

count = 1
while True:
    print("While True")
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

    data, ip = sock.recvfrom(1024)

    print("{} {}: {}".format(count, ip, data.decode()))
    count +=1

