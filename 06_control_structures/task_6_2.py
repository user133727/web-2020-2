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

test = input('Enter ip (example: 10.1.1.0): ')
ip = test.strip().split('.')
q = int(ip[0])
w = int(ip[1])
e = int(ip[2])
r = int(ip[3])

unicast = list(range(1, 224))
multicast = list(range(224, 240))
broadcast = [255,255,255,255]
unassigned = [0,0,0,0]

if q in unicast:
    print('\n','unicast','\n')
elif q in multicast:
    print('\n','multicast','\n')
elif q in broadcast and w in broadcast and e in broadcast and r in broadcast:
    print('\n','broadcast','\n')
elif q in unassigned and w in unassigned and e in unassigned and r in unassigned:
    print('\n','unassigned','\n')
else:
    print('\n','unused','\n')