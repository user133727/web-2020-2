# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

network = argv[1:]
network = ''.join(network)
ip = network[:network.find('/')]
ip = ip.split('.')
oktet1 = int(ip[0])
oktet2 = int(ip[1])
oktet3 = int(ip[2])
oktet4 = 0 * int(ip[3])

ip_template = """
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:<010b} {1:<010b} {2:<010b} {3:<010b}
"""

mask = network[network.find('/')::]
mask1 = mask.lstrip('/')
maskint = int(mask1)
maskbit = '1' * maskint
maskbit = "{:<032}".format(maskbit)
moktet1 = int(maskbit[0:8], 2)
moktet2 = int(maskbit[8:16], 2)
moktet3 = int(maskbit[16:24], 2)
moktet4 = int(maskbit[24:32], 2)

mask_template = """
Mask:
{4:<}
{0:<10} {1:<10} {2:<10} {3:<10}
{0:<10b} {1:<10b} {2:<10b} {3:<10b}
"""

print(ip_template.format(oktet1, oktet2, oktet3, oktet4))
print(mask_template.format(moktet1, moktet2, moktet3, moktet4, mask))