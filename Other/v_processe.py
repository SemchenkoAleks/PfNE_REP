#!/usr/bin/env python3

var1 = input('введите ip-адрес ')
var1='10.10.10.10/24'
x = int(var1.find('/'))
mask = var1[x:] # отрезаем от введенной строки маску
ip = var1.replace(mask,'') # отрезаем от введенной строки адрес
ip1 = ip.split('.') # разделяем ip на список

mask_math = int(mask.replace('/',''))
mask_ostatok = 32 - mask_math
mask_str = '1' * mask_math + '0' * mask_ostatok # получаем строку маски из 32 символов

template_1 = '''
Network
{:>25}{:>25}{:>25}{:>25}
{:08b}{:08b}{:08b}{:08b}
Mask
{:>25}
{:>25}{:>25}{:>25}{:>25}
{:08b}{:08b}{:08b}{:08b}
'''
