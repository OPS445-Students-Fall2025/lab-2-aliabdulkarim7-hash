#!/usr/bin/env python3
# Author: Abdulkarim Ali
# Author ID: aali394
# Date Created: 2025/09/24

import sys

# Use the first command line argument as the starting timer value
timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")

