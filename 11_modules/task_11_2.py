# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology. Если функция parse_cdp_neighbors не может обработать вывод
одного из файлов с выводом команды, надо исправить код функции в задании 11.1.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
from draw_network_graph import *
from task_11_1 import parse_cdp_neighbors

r1 = parse_cdp_neighbors('/home/std/web-2020-2/11_modules/sh_cdp_n_r1.txt')
r2 = parse_cdp_neighbors('/home/std/web-2020-2/11_modules/sh_cdp_n_r2.txt')
r3 = parse_cdp_neighbors('/home/std/web-2020-2/11_modules/sh_cdp_n_r3.txt')
sw1 = parse_cdp_neighbors('/home/std/web-2020-2/11_modules/sh_cdp_n_sw1.txt')

test = {}
test.update(r1)
test.update(r2)
test.update(r3)
test.update(sw1)

topology = {} 
lists = [] 
 
for key, value in test.items(): 
    key_str = ''.join(list(key)) 
    value_str = ''.join(list(value)) 
    if key_str not in ''.join(lists) or value_str not in ''.join(lists):
        lists.append(key_str) 
        lists.append(value_str) 
        topology[key] = value
    else:
        pass
draw_topology(topology)
