# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network = input('Введите адрес сети с префиксом(Например 10.1.1.0/24):')
ip = network[:network.find('/')]
ip = ip.split('.')
oktet1 = int(ip[0])
oktet2 = int(ip[1])
oktet3 = int(ip[2])
oktet4 = int(ip[3])

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