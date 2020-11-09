# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(addresess):
    for ip in addresess:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')
        if reply.returncode == 0:
            return True, reply.stdout
        else:
            return False, reply.stderr

if __name__ == "__main__":
    addresess = ping_ip_addresses(['google.com','ya.ru','91.219.189.148'])
    print(addresess)