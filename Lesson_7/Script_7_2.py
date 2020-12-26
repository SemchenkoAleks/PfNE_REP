#!/usr/bin/env python3

from sys import argv
f = open(argv[1])

for line in f.readlines():
    if  not line.startswith('!'):
        print(line.rstrip())

'''/home/python/Desktop/Task_PfNE/Lesson_7/config_sw1.txt'''