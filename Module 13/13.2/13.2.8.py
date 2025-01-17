# Упорядоченные дроби


# На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все
# несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.

# Формат входных данных
# На вход программе подается натуральное число n, n > 1.

# Формат выходных данных
# Программа должна вывести ответ на задачу.

# Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель
# (НОД) двух чисел. Функция реализована в модуле math.


from math import gcd
from fractions import Fraction as F

n = int(input())
result = []
while n != 1:
    for i in range(1, n):
        if gcd(i, n) == 1:
            result.append(f'{i}/{n}')
    n -= 1
answer = sorted(map(F, result))
print(*answer, sep='\n')
