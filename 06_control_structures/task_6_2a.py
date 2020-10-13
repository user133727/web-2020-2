# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Enter IP (example 10.0.1.1): ')
if ip.count('.') != 3:
    print('Incorrect IPv4 address')
elif ip.strip().split('.')[0].isdigit() is False or ip.strip().split('.')[1].isdigit() is False or ip.strip().split('.')[2].isdigit() is False or ip.strip().split('.')[3].isdigit() is False:
    print('Incorrect IPv4 address, ip must be a number')
elif int(ip.strip().split('.')[0]) not in list(range(0, 256)) or int(ip.strip().split('.')[1]) not in list(range(0, 256)) or int(ip.strip().split('.')[2]) not in list(range(0, 256)) or int(ip.strip().split('.')[3]) not in list(range(0, 256)):
    print('Incorrect IPv4 address, use only numbers in range 0-255')
else:
    ip = ip.strip().split('.')
    oktet1 = int(ip[0])
    oktet2 = int(ip[1])
    oktet3 = int(ip[2])
    oktet4 = int(ip[3])

    unicast = list(range(1, 224))
    multicast = list(range(224, 240))
    broadcast = [255,255,255,255]
    unassigned = [0,0,0,0]

    if oktet1 in unicast:
        print('This is unicast IP')
    elif oktet1 in multicast:
        print('This is multicast')
    elif oktet1 in broadcast and oktet2 in broadcast and oktet3 in broadcast and oktet4 in broadcast:
        print('This is broadcast IP')
    elif oktet1  in unassigned and oktet2 in unassigned and oktet3 in unassigned and oktet4 in unassigned:
        print('This is unassigned IP')
    else:
        print('This is unused IP')