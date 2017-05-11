#!/usr/bin/env python3

import json

config = json.loads(open('cluster.json').read())

nodes_per_host = config['nodes_per_host']

port_range_start = config['port_range_start']
port_range_end = port_range_start + nodes_per_host

# vim: sw=4 et
