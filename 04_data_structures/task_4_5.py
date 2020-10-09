# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

list0 = command1.split(' ')
list1 = list0[-1].split(',')

list01 = command2.split(' ')
list2 = list01[-1].split(',')

a = set(list1)
b = set(list2)

c = a & b
c = list(c)
c.sort()

print (c)