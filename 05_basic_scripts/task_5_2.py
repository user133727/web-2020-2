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

test = input('Enter ip and mask (example: 10.1.1.0/24): ')
ip = test.split('.')
q = str(ip[0])
w = str(ip[1])
e = str(ip[2])
r = str(ip[3][0])
bin1 = bin(int(q))
bin2 = bin(int(w))
bin3 = bin(int(e))
bin4 = bin(int(r))

mask = test[test.find('/')::]
mask1 = mask.strip('/')
mask2 = int(mask1)
bit = '1' * mask2
bit = "{:<032}".format(bit)
ex1 = int(bit[0:8], 2)
ex2 = int(bit[8:16], 2)
ex3 = int(bit[16:24], 2)
ex4 = int(bit[24:32], 2)

print('\n', 'Network:', '\n', q, '      ', w, '        ', e, '        ', r, '\n',
      bin1[2:], ' ', bin2[2:], '   ', bin3[2:], '        ', bin4[2:])

print('\n', 'Mask:', '\n', 
      mask1, '\n',
      ex1, '        ', ex2, '        ', ex3, '        ', ex4, '\n',
      bit[0:8], '   ', bit[8:16], '   ', bit[16:24], '   ', bit[24:32])