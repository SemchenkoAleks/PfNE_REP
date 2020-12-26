#!/usr/bin/env python3

from sys import argv
ignore = ["duplex", "alias", "Current configuration"]
with open(argv[1]) as src, open(argv[2], 'w') as dest:
    for line in src.readlines():
        for ign in ignore:
            if ign in line:
                break
        else:
            dest.write(line)