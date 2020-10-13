# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv
file = argv[1]
with open(file, 'r') as file:
    for line in file:
        if line.find('!') == -1 and line.find(ignore[0]) == -1 and line.find(ignore[1]) == -1 and line.find(ignore[2]) == -1:
            print(line)

# цикл