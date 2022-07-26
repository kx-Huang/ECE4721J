#!/usr/bin/python

import sys

current_node = None
current_dist = sys.maxsize * 2 + 1
node = None
neighbours = ""

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    node, parent, dist = line.split(',')
    # convert dist (currently a string) to int
    try:
        dist = int(dist)
    except ValueError:
        # dist was not a number, so silently ignore/discard this line
        continue
    if current_node == node:
        if current_dist > dist:
            current_dist = dist
        if neighbours != "":
            neighbours += ','
        neighbours += parent
    else:
        if current_node:
            # write result to STDOUT
            print('%s|%s|%s' % (current_node, str(current_dist), neighbours))
        current_dist = dist
        current_node = node
        neighbours = parent
if current_node == node:
    print('%s|%s|%s' % (current_node, str(current_dist), neighbours))
