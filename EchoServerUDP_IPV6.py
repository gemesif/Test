#!/usr/bin/env python3

import sys
import socket

#
# Test
#

#*********************************************************************************

IP = "::1"
PORT = 5000

#*********************************************************************************

# nc -u ::1 5000
# ip6tables -A OUTPUT -t nat -p udp --dport 5001 -j DNAT --to [::1]:5000
# nc -u ::1 5001
# ip6tables -t nat -L -v
# ip6tables -t nat -F

#*********************************************************************************

print('Running: {name}'.format(name=sys.argv[0]))
print('IP Address: {ipaddress} Port: {port}'.format(port=PORT, ipaddress=IP))

#*********************************************************************************

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    message = data

    print("received message:", data)
    print('received message:{message}'.format(message=data.decode()))
    print('socket address: {ip} {port}'.format(ip=addr[0], port=addr[1]))

    sock.sendto(addr[0].encode(), addr)
