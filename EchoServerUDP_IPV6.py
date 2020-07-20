#!/usr/bin/env python3

import sys
import os
import getopt
from datetime import datetime
import socket

#*********************************************************************************

#
# EchoServerUDP_IPV6.py 
# @gemesif 
# date 2020 07 16
#

#*********************************************************************************

version = '1.0'

IP = "::1"
PORT = 5000

#*********************************************************************************

# nc -u ::1 5000
# ip6tables -A OUTPUT -t nat -p udp --dport 5001 -j DNAT --to [::1]:5000
# nc -u ::1 5001
# ip6tables -t nat -L -v
# ip6tables -t nat -F

#*********************************************************************************

def myDate():
    pass
    now = datetime.now()
    s1 = now.strftime("%Y%m%d %H%M%S")
    return(s1)

#*********************************************************************************

print('ARGV      :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'hvi:p:',
        ['help',
         'version',
         'ipaddr',
         'portnumber',
         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS   :', options)
print('REMAINING :', remainder)

msg_indent = (" ".rjust(len(sys.argv[0]) + 1))

usagestring = '''\
Usage: 
{progname} [-h | --help] | [-v | --version]
{indent}[-i ipv6_address | --ipaddr ipv6_address] | [-p port_number | --portnumber port_number] 
{indent}default: ipv6_address "::1" port_number 5000
              '''.format(progname=os.path.split(sys.argv[0])[1], indent=msg_indent)

versionstring = '''\
Version: {ver}
                '''.format(ver=version)

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(usagestring)
        pass
    elif opt in ('-v', '--version'):
        print(versionstring)
        pass
    elif opt in ('-i', '--ipaddr'):
        IP = arg 
        pass
    elif opt in ('-p', '--portnumber'):
        PORT = int(arg)
        pass
       
#*********************************************************************************

cur_date = myDate()

print('Running: {name} {date}'.format(name=sys.argv[0], date=cur_date))
print('Listening - IP Address: {ipaddress} Port: {port}'.format(port=PORT, ipaddress=IP))

#*********************************************************************************

try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
except socket.error as msg:
    print("socket creation error:", msg)
    sys.exit(1)

try:
    sock.bind((IP, PORT))
except socket.error as msg:
    print("socket bind error:", msg)
    sys.exit(1)

while True:
    try:
        data, addr = sock.recvfrom(1024)
    except socket.error as msg:
        print("socket bind error:", msg)
        sys.exit(1)
    message = data

    print('Received Message:{message}'.format(message=data.decode()))
    print('Socket Address: {ip} {port}'.format(ip=addr[0], port=addr[1]))

    sock.sendto(addr[0].encode(), addr)
