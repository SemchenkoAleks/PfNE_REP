#!/usr/bin/env python3

ip_addr = input('введите  IP ')
ip_list = ip_addr.split('.')

if (
    ip_list[0].isdigit() and
    ip_list[1].isdigit() and
    ip_list[2].isdigit() and
    ip_list[3].isdigit() and
    0 <= int(ip_list[0]) <= 255 and  # ошибка - так как это происходит во время (а не до) проверки, при вводе какой-нибудь
    0 <= int(ip_list[1]) <= 255 and  # дичи код попытается сравнить дичь с числом и крашнется
    0 <= int(ip_list[2]) <= 255 and
    0 <= int(ip_list[3]) <= 255 and
    '.' in ip_addr
                               ):
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
else:
    print('Неправильный IP-адрес')