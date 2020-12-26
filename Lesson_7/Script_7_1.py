#!/usr/bin/env python3

f = open('/home/python/Desktop/Task_PfNE/Lesson_7/ospf.txt')

template = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
'''


for line in f.readlines():
    clearline1 = line.strip()
    clearline = clearline1.replace(',','')
    list = clearline.split(' ')
    print(template.format(list[-6],list[-5],list[-3],list[-2],list[-1],))