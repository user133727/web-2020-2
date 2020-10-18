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
        if not line.startswith("!"):
            ignore_line = False
            for word in ignore:
                if line.find(word) > -1:
                    ignore_line = True
                    break
            if not ignore_line:
                print(line.rstrip())

# через цикл