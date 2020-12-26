#!/usr/bin/env python3

ip_addr = input('введите  IP ')
ip_list = ip_addr.split('.')

if 0 < int(ip_list[0]) <= 223:
    print('unicast')
elif 224 <= int(ip_list[0]) <= 239:
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassignet')
else:
    print('unused')