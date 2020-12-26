#!/usr/bin/env python3

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

var1 = input('введите имя устройства ')
list0 = list(london_co[var1].keys())
list1 = ','.join(list0)
var2 = input(f'введите имя параметра ({list1}) ')
var3 = var2.lower()
print(london_co[var1].get(var3,'Parametr_ne_zadan'))