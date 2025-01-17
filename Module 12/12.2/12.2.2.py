# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква
# английского алфавита, Number – число от 0 до 99 (включительно).

# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный
# почтовый индекс Латверии.

# Примечание 1. Пример правильного (неправильного) индекса Латверии:

# AB23_56VG     # правильный
# V3F_231GT     # неправильный

# Примечание 2. Обратите внимание на символ _ в почтовом индексе.

# Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.


import random as r
import string as s


def generate_index():
    return f'{r.choice(s.ascii_uppercase)}{r.choice(s.ascii_uppercase)}{r.randint(0, 99)}_{r.randint(0, 99)}{r.choice(s.ascii_uppercase)}{r.choice(s.ascii_uppercase)}'
