# Анаграммы 2


# На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести YES, если предложения – анаграммы и NO в противном случае.

# Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.

import re

print('YES' if sorted(re.sub(r'[^a-zA-Zа-яА-Я]', '', input().lower())) == sorted(re.sub(r'[^a-zA-Zа-яА-Я]', '', input().lower())) else 'NO')
