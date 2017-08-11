#!/usr/bin/env python

s = '''##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1\tlocalhost
255.255.255.255\tbroadcasthost
::1\t\tlocalhost
'''

with open('/etc/hosts', 'w') as f:
    f.write(s)