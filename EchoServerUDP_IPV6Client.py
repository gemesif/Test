#!/usr/bin/env python3

import sys
import os
import getopt
from datetime import datetime
import socket

#*********************************************************************************

#
# EchoServerUDP_IPV6Client.py 
# @gemesif
# date 2020 07 16
#

#*********************************************************************************

version = '1.1'

IP = "::1"
# IP = "2a00:1450:400d:805::200e" # google.com
# PORT = 5001
PORT = 5000
MESSAGE = "Hello World!"
# MESSAGE = ""
LOOP = False

#*********************************************************************************

def myDate():
    pass
    now = datetime.now()
    s1 = now.strftime("%Y%m%d %H%M%S")
    return(s1)

#*********************************************************************************

print("UDP target IP:", IP)
print("UDP target port:", PORT)
print("message:", MESSAGE)

print('ARGV      :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'hvli:p:',
        ['help',
         'version',
         'loop',         
         'ipaddr',
         'portnumber',
         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS   :', options)
print('REMAINING :', remainder)

msg_indent = (" ".rjust(len(os.path.split(sys.argv[0])[1]) + 1))

usagestring = '''\
Usage:
{progname} [-h | --help] | [-v | --version] | [-l | --loop]
{indent}[-i ipv6_address | --ipaddr ipv6_address] | [-p port_number | --portnumber port_number]
{indent}defaults: ipv6_address "::1" port_number 5000
              '''.format(progname=os.path.split(sys.argv[0])[1], indent=msg_indent)

versionstring = '''\
Version: {ver}
                '''.format(ver=version)

loopstring = '''\
Running in infinite loop
             '''

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(usagestring)
        pass
    elif opt in ('-v', '--version'):
        print(versionstring) 
        pass
    elif opt in ('-l', '--loop'):
        print(loopstring)
        LOOP = True
        pass
    elif opt in ('-i', '--ipaddr'):
        IP = arg
        pass
    elif opt in ('-p', '--portnumber'):
        PORT = int(arg)
        pass

#*********************************************************************************

try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.settimeout(1)
except socket.error as msg:
    print("socket creation error:", msg)
    sys.exit(1)

try:
    sock.sendto(MESSAGE.encode(), (IP, PORT))
except socket.error as msg:
    print("socket sendto error:", msg)
    sys.exit(1)

try:
    data, ip = sock.recvfrom(1024)
except socket.error as msg:
    print("socket recvfrom error:", msg)
    sys.exit(1)

print("{}".format(data.decode()))

count = 1
while LOOP:    # infinite loop fot test
# while False:

    try:
        sock.sendto(MESSAGE.encode(), (IP, PORT))
    except socket.error as msg:
        print("socket sendto error:", msg)
        sys.exit(1)

    try:
        data, ip = sock.recvfrom(1024)
    except socket.error as msg:
        print("socket recvfrom error:", msg)
        sys.exit(1)

    print("{}".format(data).decode())
    count += 1

