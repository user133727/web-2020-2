# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку,
а затем передать строку как аргумент функции (как передать вывод команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция работать
и на других файлах (тест проверяет работу функции на выводе из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def parse_cdp_neighbors(command_output):
    with open(command_output) as file:
        command_output = file.read()
        test = {}
        command_output = command_output.split('\n')
        for line in command_output:
            name = []
            eth = []
            if line.find('>') != -1:
                main_machine = line[:line.find('>')]
            elif line.find('Eth') != -1:
                second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
                name.append(main_machine)
                eth.append(second_machine)
                main_interface = main_eth + main_inter
                second_interface = second_eth + second_inter
                name.append(main_interface)
                eth.append(second_interface)
                main_tuple = tuple(name)
                second_tuple = tuple(eth)
                test[main_tuple] = second_tuple
    return test
    
if __name__ == "__main__":
    test = parse_cdp_neighbors('/home/std/web-2020-2/11_modules/sh_cdp_n_sw1.txt')
    print(test)
