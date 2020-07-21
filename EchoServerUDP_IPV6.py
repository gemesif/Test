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

version = '1.1'

IP = "::1"
PORT = 5000

#*********************************************************************************

# nc -u ::1 5000
# ip6tables -A OUTPUT -t nat -p udp --dport 5001 -j DNAT --to [::1]:5000
# nc -u ::1 5001
# ip6tables -t nat -L -v
# ip6tables -t nat -v -L -n --line-number
# ip6tables -t nat -D OUTPUT 1
# ip6tables -t nat -F

#*********************************************************************************

def myDate():
    pass
    now = datetime.now()
    s1 = now.strftime("%Y%m%d %H%M%S")
    return(s1)

#*********************************************************************************

# print('ARGV      :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'hvdi:p:',
        ['help',
         'version',
         'document',
         'ipaddr',
         'portnumber',
         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

# print('OPTIONS   :', options)
# print('REMAINING :', remainder)

msg_indent = (" ".rjust(len(os.path.split(sys.argv[0])[1]) + 1))

usagestring = '''\
Usage: 
{progname} [-h | --help] | [-v | --version] | | [-d | --document]
{indent}[-i ipv6_address | --ipaddr ipv6_address] | [-p port_number | --portnumber port_number] 
{indent}defaults: ipv6_address "::1" port_number 5000
              '''.format(progname=os.path.split(sys.argv[0])[1], indent=msg_indent)

versionstring = '''\
Version: {ver}
                '''.format(ver=version)

docstring = '''\
Documentation: {ver}
### Goal.
IPv6 address discovery of host in IP network communication.
### Realization.
Client-server architecture. Client(IPv6EchoClient) send request to server(Pv6Echo), the server sends her reply to client, what was the ip adders which client used.
My solution the IPv6 Echo.py, IPv6EchoClient.py pair, written in Python programming language. Using UDP protocoll.
### Parametrization.
```
{help}
```
### Usage instruction tricks.
If the server and client in the same host, we can detect the client actual Global Unicast IPv6  Address(ipv6 or temporary ipv6...).

(The example is in Linux-Ubuntu 20.04 LTS environment)

The method:

iptables rule

```ip6tables -A OUTPUT -t nat -p udp --dport 5001 -j DNAT --to [::1]:5000```

(forward from port 5001 to [::1]:5000 ipaddress, port in OUTPUT chain, nat table)

```\# ip6tables -t nat -v -L -n --line-number```

(list nat table rules)

```\# ip6tables -t nat -D OUTPUT 1```

(delete rule #1 from OUTPUT chain nat table) 

Starting the server

```EchoServerUDP_IPV6.py -p 5000```

Starting the client

```EchoServerUDP_IPV6Client.py -i 2a00:1450:400d:805::200e -p 5001 # google.com IPv6 address```


            '''.format(ver=version, help=usagestring)

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(usagestring)
        exit(0)
    elif opt in ('-v', '--version'):
        print(versionstring)
        exit(0)
    elif opt in ('-d', '--document'):
        print(docstring)
        exit(0)
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
    print(addr[0])
