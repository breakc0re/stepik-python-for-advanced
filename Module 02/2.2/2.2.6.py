# Задача: Произведение чисел


n = int(input())  # количество чисел в наборе
numbers = []  # список чисел из набора

# Ввод чисел набора
for _ in range(n):
    num = int(input())
    numbers.append(num)

target = int(input())  # число, которое нужно проверить

found = False  # флаг для обозначения нахождения числа

# Проверка произведения чисел
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] * numbers[j] == target:
            found = True
            break
    if found:
        break

if found:
    print("ДА")
else:
    print("НЕТ")
