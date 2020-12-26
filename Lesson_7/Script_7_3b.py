#!/usr/bin/env python3

template = '{:>15} {:>15} {:>15}'
mac_table = []
user_vlan = input('Enter VLAN number: ')

with open('/home/python/Desktop/Task_PfNE/Lesson_7/CAM_table.txt') as f:
    for line in f.readlines():
        list1 = line.split()
        if list1 and list1[0].isdigit() and list1[0] == user_vlan:
            vlan, mac, _, intf = list1
            print(template.format(vlan, mac, intf))
