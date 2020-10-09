# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

test = [
['switchport mode access',
 'switchport access vlan {}',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable'],
['switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk allowed vlan {}']
]

modes = [
['Enter VLAN number:'],
['Enter allowed VLANs:']
]

mode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface and number: ')
mode = mode.count('trunk')
vlans = input (' '.join(modes[mode]))
print('interface {}'.format(interface))
print('\n'.join(test[mode]).format(vlans))