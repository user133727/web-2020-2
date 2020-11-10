# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    trunk = {}
    access = {}
    with open('/home/std/pyneng-examples-exercises/exercises/09_functions/config_sw1.txt', 'r') as f:
         for line in f:
            if line.find('interface') != -1:
                interface=line.strip().split()[1]
                f.readline()
                line=f.readline() 
                if line.find('switchport access vlan') != -1:
                    line=line.strip()
                    vlan=line.split()[-1]
                    access[interface]=vlan
                elif line.find('switchport trunk allowed vlan') != -1:    
                    line=line.strip().split()
                    vlan=line[4].split(';')
                    trunk[interface]=vlan
    return access,trunk  
              
print(get_int_vlan_map('/home/std/pyneng-examples-exercises/exercises/09_functions/config_sw1.txt'))