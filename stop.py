#!/usr/bin/env python3

import os
import os.path
import signal
import traceback

exec(open('common.py').read())

for port in range(port_range_start, port_range_end):
    pid_path = os.path.join(str(port), 'pid')
    try:
        with open(pid_path) as pid_file:
            pid = int(pid_file.read())
            os.kill(pid, signal.SIGTERM)
            os.remove(pid_path)
    except:
        traceback.print_exc()

# vim: sw=4 et
