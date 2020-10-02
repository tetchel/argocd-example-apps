#!/usr/bin/env python3

import sys
from datetime import datetime
import time

def print_time():
    now = datetime.now()
    print("It's {}".format(now.strftime('%d/%m/%Y %H:%M:%S')))
    time.sleep(1)

INF = 'inf'

if len(sys.argv) > 1:
    count_arg = sys.argv[1]
    if count_arg == INF or count_arg == '-1':
        count = INF
    else:
        count = int(count_arg)
else:
    count = 10

if count == INF:
    print('Counting forever')
    while True:
        print_time()
else:
    print('Counting for {}s'.format(count))
    for i in range(count):
        print_time()
