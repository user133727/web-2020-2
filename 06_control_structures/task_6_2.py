# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter IP (example 10.0.1.1): ')
ip = ip.strip().split('.')
oktet1 = int(ip[0])
oktet2 = int(ip[1])
oktet3 = int(ip[2])
oktet4 = int(ip[3])

unicast = list(range(1, 224))
multicast = list(range(224, 240))
broadcast = [255,255,255,255]
unassigned = [0,0,0,0]

if oktet1 in unicast:
    print('This is unicast IP')
elif oktet1 in multicast:
    print('This is multicast')
elif oktet1 in broadcast and oktet2 in broadcast and oktet3 in broadcast and oktet4 in broadcast:
    print('This is broadcast IP')
elif oktet1  in unassigned and oktet2 in unassigned and oktet3 in unassigned and oktet4 in unassigned:
    print('This is unassigned IP')
else:
    print('This is unused IP')