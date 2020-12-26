#!/usr/bin/env python3

template = '{:>15} {:>15} {:>15}'

with open('/home/python/Desktop/Task_PfNE/Lesson_7/CAM_table.txt') as f:
    for line in f.readlines():
        list1 = line.split()
        if list1[0].isdigit():
            print(template.format(list1[0], list1[1], list1[3]))
        else:
            pass