#!/usr/bin/env python3

import os
import os.path
import shutil

exec(open('common.py').read())

for port in range(port_range_start, port_range_end):
    os.mkdir(str(port))
    redis_conf_path = os.path.join(str(port), 'redis.conf')
    shutil.copy('redis.conf', redis_conf_path)
    open(redis_conf_path, 'a').write('port ' + str(port))

# vim: sw=4 et
