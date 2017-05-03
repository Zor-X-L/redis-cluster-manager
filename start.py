#!/usr/bin/env python3

import subprocess
import os.path

exec(open('common.py').read())

for port in range(port_range_start, port_range_end):

    process = subprocess.Popen(
            args=[os.path.join('..', 'redis-server'), 'redis.conf'],
            cwd=str(port),
            stdout=open(os.path.join(str(port), 'stdout'), 'a'),
            stderr=open(os.path.join(str(port), 'stderr'), 'a'))

    pid_file = open(os.path.join(str(port), 'pid'), 'w')
    pid_file.write(str(process.pid))

# vim: sw=4 et
