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

#websites_to_block = ['youtube.com', 'm.facebook.com', 'facebook.com', 'crunchyroll.com', 'reddit.com', 'yahoo.com', 'generals.io', 'kissanime.ru', 'solarmoviez.to', 'thepiratebay.org', 'yts.ag', 'penpalworld.com', 'kissanime.io']
with open('block-list') as f:
    websites_to_block = [l.strip() for l in f.readlines()]

with open('/etc/hosts', 'w') as f:
    f.write(s)
    for website in websites_to_block:
        f.write('127.0.0.1 %s\n' % website)
        f.write('127.0.0.1 www.%s\n' % website)
