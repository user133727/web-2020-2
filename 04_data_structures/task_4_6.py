# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3 3d18h FastEthernet0/0"

print('\n'' Prefix','\t\t', ospf_route.split(' ')[6],'\n','AD/Metric', '\t\t', ospf_route.split(' ')[7][1:7], '\n',
'Next-Hop', '\t\t', ospf_route.split(' ')[9], '\n', 'Last update', '\t\t', ospf_route.split(' ')[10], '\n', 
'Outbound Interface', '\t', ospf_route.split(' ')[11], '\n')