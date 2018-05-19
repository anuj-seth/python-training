#!/usr/bin/env python

import re

fobj = open('/var/log/syslog', 'r')

for line in fobj:
    fields = line.split(' ')
    print(re.sub('(\[[0-9]*\])*:$', '', fields[4]))
