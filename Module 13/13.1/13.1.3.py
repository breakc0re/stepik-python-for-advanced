# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.


from decimal import *

num = Decimal(input())
minimum = 9
maximum = 0

for i in str(num):
    if i.isdigit():
        if int(i) > maximum:
            maximum = int(i)
        if int(i) < minimum:
            minimum = int(i)
print(int(minimum) + int(maximum))
