# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    return any(word in command for word in ignore)

def convert_config_to_dict(command, ignore):
    conf={}
    with open('/home/std/pyneng-examples-exercises/exercises/09_functions/config_sw1.txt', 'r') as f:
        for line in f:
            if line.find('!') == -1:
                if not ignore_command(line, ignore):
                    if not line.startswith(' '):
                        upp=line.strip()
                        conf[upp] = []
                    else:
                        conf[upp].append(line.strip())
    return conf

print(convert_config_to_dict('/home/std/pyneng-examples-exercises/exercises/09_functions/config_sw1.txt',ignore))
