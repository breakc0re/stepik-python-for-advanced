# Задача: Назад, вперёд и наоборот

numbers = [int(n) for n in input().split()]

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(*numbers)
