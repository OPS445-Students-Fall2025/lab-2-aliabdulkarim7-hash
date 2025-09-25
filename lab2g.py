#!/usr/bin/env python3
# Author: Abdulkarim Ali
# Author ID: aali394
# Date Created: 2025/09/24

import sys

# Default timer is 3 when no argument is provided
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')

