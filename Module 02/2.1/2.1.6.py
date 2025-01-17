# Задача: Переворот числа

number = input()

if len(number) <= 5:
    number = int(number[::-1])
    print(number)
elif len(number) > 5:
    number = number[0] + number[:0:-1]
    print(number)
