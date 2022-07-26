#!/usr/bin/python

import sys
import math

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split('|')
    # split into neighbours
    neigh = words[2].split(',')
    dist = int(words[1])
    print(words[0]+','+words[0]+','+str(dist))
    for n in neigh:
        if n != words[0]:
            print(n+','+words[0]+','+str(dist+1))
