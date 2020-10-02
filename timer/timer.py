#!/usr/bin/env python3

import sys
from datetime import datetime
import time

if (len(sys.argv) > 1):
    count = int(sys.argv[1])
else:
    count = 10

print('Count is {}'.format(count))

for i in range(count):
    now = datetime.now()
    print("It's {}".format(now.strftime('%d/%m/%Y %H:%M:%S')))
    time.sleep(1)
