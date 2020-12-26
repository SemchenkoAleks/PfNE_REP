#!/usr/bin/env python3

int_mode = input('Введите режим работы интерфейса (access/trunk): ')

dict2 = {
   'access': 'Введите VLAN: ',
   'trunk': 'Введите номера разрешенных VLANов: '
}

int_type = input('Введите тип и номер интерфейса: ')
vlans = input(dict2.get(int_mode))

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

first_string = 'interface ' + int_type

command_access = [
   first_string,
   access_template[0],
   access_template[1].format(vlans),
   access_template[2],
   access_template[3],
   access_template[4],
]

command_trunk = [
   first_string,
   trunk_template[0],
   trunk_template[1],
   trunk_template[2].format(vlans),
]

dict1 = {
   'access': '\n'.join(command_access),
   'trunk': '\n'.join(command_trunk)
}
print(dict1.get(int_mode))