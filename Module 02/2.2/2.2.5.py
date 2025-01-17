# Задача: Различные элементы

numbers = [int(n) for n in input().split()]
print(len(set(numbers)))

# однострочное решение

# print(len(set(input().split())))

# еще одно решение, не используя множества.

# numbers = input().split()
# counter = 1
#
# for i in range(len(numbers) - 1):
#     if numbers[i] != numbers[i + 1]:
#         counter += 1
#
# print(counter)
