# IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

# Напишите функцию generate_ip(), которая с помощью модуля random генерирует и возвращает случайный
# корректный IP адрес.

# Примечание 1. Пример правильного (неправильного) IP адреса:

# 192.168.5.250        # правильный
# 199.300.521.255      # неправильный

# Примечание 2. Вызывать функцию generate_ip() не нужно, требуется только реализовать.


import random


def generate_ip():
    return f'{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}'
