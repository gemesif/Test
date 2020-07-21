*Documentation: 1.1*
### Goal.
IPv6 address discovery of host in IP network communication.
### Realization.
Client-server architecture. Client(IPv6EchoClient) send request to server(Pv6Echo), the server sends her reply to client, what was the ip adders which client used.
My solution the IPv6 Echo.py, IPv6EchoClient.py pair, written in Python programming language. Using UDP protocoll.
### Parametrization.
```
Usage: 
EchoServerUDP_IPV6.py [-h | --help] | [-v | --version] | | [-d | --document]
                      [-i ipv6_address | --ipaddr ipv6_address] | [-p port_number | --portnumber port_number] 
                      defaults: ipv6_address "::1" port_number 5000
              
```
### Usage instruction tricks.
If the server and client in the same host, we can detect the client actual Global Unicast IPv6  Address(ipv6 or temporary ipv6...).
(The example is in Linux-Ubuntu 20.04 LTS environment)

#### The method:

iptables rule

```ip6tables -A OUTPUT -t nat -p udp --dport 5001 -j DNAT --to [::1]:5000```

(forward from port 5001 to [::1]:5000 ipaddress, port in OUTPUT chain, nat table)

```# ip6tables -t nat -v -L -n --line-number```

(list nat table rules)

```# ip6tables -t nat -D OUTPUT 1```

(delete rule #1 from OUTPUT chain nat table) 

Starting the server

```EchoServerUDP_IPV6.py -p 5000```

Starting the client

```EchoServerUDP_IPV6Client.py -i 2a00:1450:400d:805::200e -p 5001 # google.com IPv6 address```


            
