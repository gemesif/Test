#!/usr/bin/python3

from datetime import datetime
import re
import netifaces
import ipaddress

# *************************************************************************************************************


def myDate():
    pass
    now = datetime.now()
    s1 = now.strftime("%Y%m%d %H%M%S")
    return(s1)

# *************************************************************************************************************

binary_to_hex = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "a",
    "1011": "b",
    "1100": "c",
    "1101": "d",
    "1110": "e",
    "1111": "f"}

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"}

bit_inverse = {
    "0": "1",
    "1": "0"
}

"""
print(binary_to_hex)

print("#****************************")

print(binary_to_hex[hex_to_binary["0"]])
print(binary_to_hex[hex_to_binary["1"]])
print(binary_to_hex[hex_to_binary["2"]])
print(binary_to_hex[hex_to_binary["3"]])
print(binary_to_hex[hex_to_binary["4"]])
print(binary_to_hex[hex_to_binary["5"]])
print(binary_to_hex[hex_to_binary["6"]])
print(binary_to_hex[hex_to_binary["7"]])
print(binary_to_hex[hex_to_binary["8"]])
print(binary_to_hex[hex_to_binary["9"]])
print(binary_to_hex[hex_to_binary["a"]])
print(binary_to_hex[hex_to_binary["b"]])
print(binary_to_hex[hex_to_binary["c"]])
print(binary_to_hex[hex_to_binary["d"]])
print(binary_to_hex[hex_to_binary["e"]])
print(binary_to_hex[hex_to_binary["f"]])
"""

# *************************************************************************************************************


def bit_masking(bit, mask_bit):

    res = '0'

    if bit == '0' and bit == '0':
        pass
    if bit == '0' and mask_bit == '0':
        pass
        res = '0'
    elif bit == '0' and mask_bit == '1':
        res = '0'
    elif bit == '1' and mask_bit == '0':
        res = '0'
    elif bit == '1' and mask_bit == '1':
        res = '1'

    return(res)

# *************************************************************************************************************


class Host_MAC:
    interface = {}

# *************************************************************************************************************


class Host_ipv6:
    date = ''
    interfaces = []
    interface_data = {}
    """
date
interfaces
interface_data
    interface_name:
    [
    [ipv6, netmask, netmaskCIDR, network, interfaceID]
    ]

   """

# *************************************************************************************************************


def ipv6_hex_to_binary(ip):

    ip_exploded_nosep = "".join(ipaddress.ip_address(ip).exploded.split(":"))
    ip_exploded_nosep_1hex = [(ip_exploded_nosep[i:i + 1])
                              for i in range(0, len(ip_exploded_nosep), 1)]

    res_array = []
    for s in ip_exploded_nosep_1hex:
        ss = hex_to_binary[s].rjust(4, "0")
        res_array.append(ss)
        # print(ss)

    ip_bin = "".join(res_array)
    return(ip_bin)


def get_machine_interfaces():

    res_array = []
    for interface in netifaces.interfaces():
        res_array.append(interface)
        # print(interface)

    return(res_array)

# *************************************************************************************************************


def ipv6_binary_to_hex(ip):

    ip_4bin = [(ip[i:i + 4]) for i in range(0, len(ip), 4)]

    res_array = []
    res_string = ""
    for s in ip_4bin:
        ss = binary_to_hex[s]
        #print("++++++++++++++++++", ss)
        res_array.append(ss)

        res_string += ss

    ip_hex = ":".join([(res_string[i:i + 4])
                       for i in range(0, len(res_string), 4)])
    return(ip_hex)

# *************************************************************************************************************


def ipv6_hex_netmask_to_CIDR(netmask):

    return(ipv6_hex_to_binary(ipaddress.IPv6Address(netmask).exploded).count('1'))

# *************************************************************************************************************


def ipv6_CIDR_netmask_to_binary(netmask):

    return('1'.rjust(netmask, '1').ljust(128, '0'))

# *************************************************************************************************************


def ipv6_CIDR_netmask_to_reversebinary(netmask):

    return('0'.rjust(netmask, '0').ljust(128, '1'))

# *************************************************************************************************************


def ipv6_nodeID(ip, cidr):

    pass
    tmp_ip = ipv6_hex_to_binary(ip)
    tmp_mask = ipv6_CIDR_netmask_to_reversebinary(cidr)
    # print(tmp_ip, tmp_mask, sep='####')
    # print(len(tmp_mask))

    length = len(tmp_ip)

    res = ""
    for i in range(length):
        pass
        res = res + bit_masking(tmp_ip[i], tmp_mask[i])

    res = ipv6_binary_to_hex(res)

    return(res)


# *************************************************************************************************************

def ipv6_network_from_ipaddress_CIDR(ip, cidr):

    pass
    tmp_ip = ipv6_hex_to_binary(ip)
    tmp_cidr = ipv6_CIDR_netmask_to_binary(cidr)  # Mas nevet adni: mask
    # print(tmp_ip, tmp_cidr, sep='####')
    # print(len(tmp_cidr))

    length = len(tmp_ip)

    res = ""
    for i in range(length):
        pass
        res = res + bit_masking(tmp_ip[i], tmp_cidr[i])

    res = ipv6_binary_to_hex(res)

    return(res)

# *************************************************************************************************************


def get_machine_ipv6(interface):

    try:
        addrs = netifaces.ifaddresses(interface)
        # print(addrs[netifaces.AF_INET6])
        ipv6_addrs_line = addrs[netifaces.AF_INET6]

    except BaseException:
        print("Something went wrong: " + "get_machine_ipv6()")
        return 1
        pass

    res_array = []
    for line in ipv6_addrs_line:
        ipv6_addr = line['addr']

        if(re.search('%', ipv6_addr)):
            ipv6_addr = ipv6_addr.split('%')[0]
        else:
            pass

        ipv6_addr = ipaddress.IPv6Address(ipv6_addr).exploded
        netmask = line['netmask']

        res_array += [[ipv6_addr, netmask]]

        #print(ipv6_addr, netmask, sep="   ")

    return(res_array)

# *************************************************************************************************************

# print(get_machine_interfaces())
# print(get_machine_ipv6('eth0'))

"""
NETWORKS = [
    '10.9.0.0/24',
    '10.9.0.3/24',
    'fdfd:87b5:b475:5e3e::/64',
    '2a01:036d:0119:4da6:e839:4b4b:c8d9:f7ef'
]

for n in NETWORKS:
    net = ipaddress.ip_network(n, strict=False)
    print('{!r}'.format(net))
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net):
    # for ip in  net:
        print(ip)
    print()
"""
# *************************************************************************************************************

"""
iface = ipaddress.ip_interface('2a01:036d:0119:48cd:4028:54ec:f061:814c/64')
#iface = ipaddress.ip_interface('2a01:036d:0119:48cd:4028:54ec:f061:814c/ffff:ffff:ffff:ffff::')
print("ipaddress test................")
print(iface)
print(iface.network)
print(iface.netmask)
print(iface.ip)
"""

# *************************************************************************************************************
"""
print("network interface ID")

netmask_bin = ipv6_hex_to_binary("ffff:ffff:ffff:ffff::")
netmask_CIDR = netmask_bin.count('1')
print("++++++++++++++", netmask_bin, "   ", netmask_CIDR)
netmask_hex =  ipv6_binary_to_hex(netmask_bin)
print("++++++++++++++", netmask_hex)

ipv6_binary_to_hex(netmask_bin)

print("test ip to.................")
ip = "2a01:36d:119:4e9f:d13b:1e03:fc96:798c"
print(ipaddress.IPv6Address(ip).exploded)
ip_bin = ipv6_hex_to_binary(ip)
print(ip_bin)
ip = ipv6_binary_to_hex(ip_bin)
print(ip)
"""
# *************************************************************************************************************

"""
print("network interface ip")
temp_ip = get_machine_ipv6('eth0')
for li in temp_ip:
   temp_li = li
   #print(temp_li[0], temp_li[1], ipv6_hex_netmask_to_CIDR(temp_li[1]), sep='#')
   #print(ipv6_CIDR_netmask_to_binary(64))
   pass
"""
ipv6_network_from_ipaddress_CIDR('2a01:036d:0119:2d34:c0c1:d8e8:66a2:1f09', 65)
#ipv6_network_from_ipaddress_CIDR('0000:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 21)
#ipv6_network_from_ipaddress_CIDR('1111:1111:1111:1111:1111:1111:1111:1111', 2)
#ipv6_network_from_ipaddress_CIDR('0000:1111:1111:1111:1111:1111:1111:1111', 65)

# *************************************************************************************************************
"""
print("netmask")
print(ipv6_CIDR_netmask_to_binary(16))
print(ipv6_CIDR_netmask_to_reversebinary(16))
print(ipv6_CIDR_netmask_to_binary(0))
print(ipv6_CIDR_netmask_to_reversebinary(0))
"""
"""
print("date")
print(myDate())
"""
"""
print("test")
test(test1)
print(myDate())
"""

#**************************************************************************************************************

def MAC_store(interface):

    myHost_MAC = Host_MAC()
    myHost_MAC.interface = {
    interface: netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']}

    return(myHost_MAC)

#**************************************************************************************************************

def IPV6_store(interface):
    pass
    myHost = Host_ipv6()
    myHost.date = myDate()
    myHost.interfaces = get_machine_interfaces()
    myHost.interface_data = {interface: get_machine_ipv6(interface)}

    for i in range(len(myHost.interface_data[interface])):
        pass
        # print(i)
        myHost.interface_data[interface][i] += [
            ipv6_hex_netmask_to_CIDR(
                myHost.interface_data[interface][i][1])]
        # print(myHost.interface_data[interface][i][0])
        # print(myHost.interface_data[interface][i][2])
        myHost.interface_data[interface][i] += [
            ipv6_network_from_ipaddress_CIDR(
                myHost.interface_data[interface][i][0],
                myHost.interface_data[interface][i][2])]
        myHost.interface_data[interface][i] += [
            ipv6_nodeID(
                myHost.interface_data[interface][i][0],
                myHost.interface_data[interface][i][2])]

    return(myHost)

#**************************************************************************************************************

def print_IPV6_store_for_log(store):

    pass
    #print(store.interface_data)
    tmp_date =  myDate()

    print("#***********************************interface data***************************************************")

    for key in store.interface_data:
        #print(key)
        for i in range(len(store.interface_data[key])):
            pass
            #print(store.interface_data[key][i])
            #[ipv6, netmask, netmaskCIDR, network, interfaceID]
            #print(i)
            """
            myorder = "I have a {carname}, it is a {model}."
            #print(myorder.format(carname = "Ford", model = "Mustang"))
            """
            printing = "{date}#{interface}#{ipv6}#{netmaskCIDR}#{network}#{interfaceID}"
            tmp_interface = key 
            tmp_ipv6 = store.interface_data[key][i][0]
            tmp_netmaskCIDR = store.interface_data[key][i][2]
            tmp_network = store.interface_data[key][i][3]
            tmp_interfaceID = store.interface_data[key][i][4]
            print(printing.format(date = tmp_date, interface = tmp_interface, ipv6 = tmp_ipv6, 
                netmaskCIDR = tmp_netmaskCIDR, network = tmp_network, interfaceID = tmp_interfaceID))

#**************************************************************************************************************

#my_MAC = MAC_store('eth0')
#print(my_MAC.interface['eth0'])


# print(get_machine_interfaces())
# print(get_machine_ipv6('eth0'))

interface = 'eth0'
addrs = netifaces.ifaddresses(interface)
interface_MAC = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']

myHost_MAC = Host_MAC()

myHost_MAC.interface = {
    interface: netifaces.ifaddresses(interface)[
        netifaces.AF_LINK][0]['addr']}

#print(myHost_MAC.interface)

myHost_IPV6 = IPV6_store('eth0')

myHost = Host_ipv6()
myHost.date = myDate()
myHost.interfaces = get_machine_interfaces()
# print(myHost.interfaces)
myHost.interface_data = {interface: get_machine_ipv6(interface)}
# ipv6_network_from_ipaddress_CIDR()
#myHost.interface_data[interface][1] += [ipv6_hex_netmask_to_CIDR(myHost.interface_data[interface][1][1])]

for i in range(len(myHost.interface_data[interface])):
    pass
    # print(i)
    myHost.interface_data[interface][i] += [
        ipv6_hex_netmask_to_CIDR(
            myHost.interface_data[interface][i][1])]
    # print(myHost.interface_data[interface][i][0])
    # print(myHost.interface_data[interface][i][2])
    myHost.interface_data[interface][i] += [
        ipv6_network_from_ipaddress_CIDR(
            myHost.interface_data[interface][i][0],
            myHost.interface_data[interface][i][2])]
    myHost.interface_data[interface][i] += [
        ipv6_nodeID(
            myHost.interface_data[interface][i][0],
            myHost.interface_data[interface][i][2])]

# print(myHost.date)
#print(myHost.interfaces)
# print(myHost.interface_data)
# print(myHost.interface_data[interface][0])
# print(myHost.interface_data[interface][1])
# print(myHost.interface_data[interface][2])
# print(myHost)


#print(myHost_IPV6.date)
#print(myHost_IPV6.interfaces)
#print(myHost_IPV6.interface_data)
#print(myHost_IPV6.interface_data[interface][0])
#print(myHost_IPV6.interface_data[interface][1])
#print(myHost_IPV6.interface_data[interface][2])
#print(myHost_IPV6)

print_IPV6_store_for_log(myHost_IPV6)
