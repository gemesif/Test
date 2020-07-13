#!/usr/bin/env python3

import socket

UDP_IP = "::1"
UDP_PORT = 5000

# nc -u ::1 5000
# ip6tables -A OUTPUT -t nat -p udp --dport 5001 -j DNAT --to [::1]:5000
# nc -u ::1 5001
# ip6tables -t nat -L -v
# ip6tables -t nat -F

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    message = data

    print("received message:", data)
    print("addr:", addr[0], addr[1], sep=' ')

    sock.sendto(addr[0].encode(), addr)

