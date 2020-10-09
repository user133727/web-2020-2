# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

file = open('/home/std/pyneng-examples-exercises/exercises/07_files/ospf.txt')
for line in file:
    cont=line.split(' ') 
    print('\n'' Prefix','\t\t', cont[8],'\n','AD/Metric', '\t\t', cont[9], '\n',
    'Next-Hop', '\t\t', cont[10], '\n', 'Last update', '\t\t', cont[11], '\n',
    'Outbound Interface', '\t', cont[12], '\n')

