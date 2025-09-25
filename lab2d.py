#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

name = sys.argv[1]         # string
age = int(sys.argv[2])     # integer

print("Hi " + name + ", you are " + str(age) + " years old.")



