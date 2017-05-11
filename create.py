#!/usr/bin/env python3

import subprocess

exec(open('common.py').read())

args = ['./redis-trib.rb', 'create', '--replicas', str(config['replicas'])]

for host in config['hosts']:
    for port in range(port_range_start, port_range_end):
        args.append(host + ':' + str(port))

subprocess.call(args)

# vim: sw=4 et
