#!/usr/bin/env python3

from sys import argv
f = open(argv[1])

ignore = ["duplex", "alias", "Current configuration"]

for line in f.readlines():
    for ign in ignore:
        if line.startswith('!') or ign in line:
            break
    else:
        print(line.rstrip())