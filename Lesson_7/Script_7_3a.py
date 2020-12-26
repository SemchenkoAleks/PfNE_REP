#!/usr/bin/env python3

template = '{:>15} {:>15} {:>15}'
mac_table = []

with open('/home/python/Desktop/Task_PfNE/Lesson_7/CAM_table.txt') as f:
    for line in f.readlines():
        list1 = line.split()
        if list1 and list1[0].isdigit():
            vlan, mac, _, intf = list1
            mac_table.append([int(vlan), mac, intf])

    for vlan, mac, intf in sorted(mac_table):
        print(template.format(vlan, mac, intf))