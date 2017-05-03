#!/usr/bin/env python3

import socket
import fcntl
import struct
import json
import ipaddress
import os
import os.path
import shutil

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, # SIOCGIFADDR
            struct.pack('256s', bytes(ifname[:15], 'utf-8'))
            # Python 2.7: remove the second argument for the bytes call
        )[20:24])

config = json.loads(open('cluster.json').read())

network = ipaddress.ip_network(config['network'])

for (index, ifname) in socket.if_nameindex():
    ip = get_interface_ip(ifname)
    if ipaddress.ip_address(ip) in network:
        break

num_nodes = config['host_to_num_nodes'][ip]

port_range_start = config['port_range_start']
port_range_end = port_range_start + num_nodes

# vim: sw=4 et
