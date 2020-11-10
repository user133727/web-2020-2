# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_access_config(intf_vlan_mapping,  trunk_template):
    list=[]
    list_test={}
    for inter, vlan in intf_vlan_mapping.items():
        list.append('interface {}'.format(inter))
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                line =line + ' {}'
                vl = [str(vlan1) for vlan1 in intf_vlan_mapping[inter]]
                list.append(line.format(' '.join(vl)))
            else:
                list.append(line)
        list_test[inter] = list
        list=[]
    return list_test

print(generate_access_config(trunk_config, trunk_mode_template))