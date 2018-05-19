#!/usr/bin/env python

import sys
import itertools
from random import randrange
import datetime 

def ip_range(input_string):
    octets = input_string.split('.')
    chunks = [map(int, octet.split('-')) for octet in octets]
    ranges = [range(c[0], c[1] + 1) if len(c) == 2 else c for c in chunks]

    return ['.'.join(map(str, address)) for address in itertools.product(*ranges)]

def generate_ip_addresses():
    return ip_range('10.17.1-10.1-10')

def random_date(start,l):
    current = start
    while l >= 0:
        #curr = current + datetime.timedelta(minutes=randrange(60))
        #yield curr
        current = current + datetime.timedelta(seconds=randrange(60))
        yield current
        l-=1

start_date = datetime.datetime(2017, 9, 20, 13, 00)
ip_addresses = generate_ip_addresses()
trx_type = ['create_account', 'delete_account', 'download_file', 'buy_gold', 'sell_stocks']


with open('out_file.log', 'w') as log_file:
    log_file.write('timestamp;ip_address;trx_type;response_time\n')
    for x in random_date(start_date, int(sys.argv[1])):
        timestamp = x.strftime("%d/%m/%Y %H:%M")
        ip_addr = ip_addresses[randrange(100)]
        trx = trx_type[randrange(5)]
        resp_time = randrange(50)
        log_file.write('{0};{1};{2};{3}\n'.format(timestamp, ip_addr, trx, resp_time))
                                   
        
                


