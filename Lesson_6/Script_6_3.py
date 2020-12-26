#!/usr/bin/env python3

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}


for intf_tr, vlan_tr in trunk.items():
    print("interface FastEthernet" + intf_tr)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            if vlan_tr[0] == 'add':
                print('\n'.join(trunk_template) + ' add ' + ','.join(vlan_tr[1:]))
            elif vlan_tr[0] == 'only':
                print('\n'.join(trunk_template) + ' ' + ','.join(vlan_tr[1:]))
            elif vlan_tr[0] == 'del':
                print('\n'.join(trunk_template) + ' remove ' + ','.join(vlan_tr[1:]))