# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv
file = argv[1]
test1 = file[0]
test2 = file [1]
with open(test1, 'r') as file, open(test2, 'a') as output:
    for line in file:
        if line.find(ignore[0]) == -1 and line.find(ignore[1]) == -1 and line.find(ignore[2]) == -1:
            output.write(line)