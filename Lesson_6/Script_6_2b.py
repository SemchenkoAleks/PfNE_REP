#!/usr/bin/env python3

while True:
    ip_addr = input('введите  IP ')
    ip_list = ip_addr.split('.')
    Correct_ip = True
    for octet in ip_list:
        if not (octet.isdigit() and int(octet) in range(256)):  # если октет не число, то на совпадение ренджу
            Correct_ip = False       # проверки уже не будет и код не крашнется
            break
    if Correct_ip:
        break
    print("Incorrect IPv4 address")

if 0 < int(ip_list[0]) <= 223:
    print('unicast')
elif 224 <= int(ip_list[0]) <= 239:
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassigned')
else:
    print('unused')