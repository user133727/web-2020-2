# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(addresses):
    new_add = []
    for ip in addresses:
        if ip.find('-') !=-1 and ip.count('.') >3:
            ip = ip.split('-')
            ip1 = ip[0].split('.')
            ip2 = ip[1].split('.')
            ip = []
            if ip1[2] != ip2[2]:
                for n in range(int(ip2[2])-int(ip1[2])+1): #подсчёт разности 
                    if n==0:
                        new_ip = [ip1[0]+'.'+ip1[1]+'.'+str(int(ip1[2])+int(n))+'.'+str((int(a)+int(ip1[3]))) for a in range(255-int(ip1[3])+1)]
                        ip.extend(new_ip)
                    elif int(ip1[2])+n != int(ip2[2]):
                        new_ip = [ip1[0]+'.'+ip1[1]+'.'+str(int(ip1[2])+int(n))+'.'+str(a) for a in range(255+1)]
                        ip.extend(new_ip)
                    else:
                        new_ip = [ip1[0]+'.'+ip1[1]+'.'+str(int(ip1[2])+int(n))+'.'+str(a) for a in range(int(ip2[3])+1)]
                        ip.extend(new_ip)
            elif ip1[3] != ip2[3]:
                ip = [ip1[0]+'.'+ip1[1]+'.'+ip1[2]+'.'+str((int(a)+int(ip1[3]))) for a in range(int(ip2[3])-int(ip1[3])+1)]
            new_add.extend(ip)
        elif ip.find('-') !=-1:
            ip = ip.split('-')
            new_ip = ip[1]
            ip = ip[0].split('.')
            ip = [ip[0]+'.'+ip[1]+'.'+ip[2]+'.'+str((int(a)+int(ip[3]))) for a in range(int(new_ip)-int(ip[3])+1)]
            new_add.extend(ip)
        else:
            new_add.append(ip)
    return new_add
if __name__ == "__main__":
    ip = convert_ranges_to_ip_list(['8.8.4.4-8.8.5.2'])
    print(ip)