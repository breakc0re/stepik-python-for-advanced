# Задача: Больше предыдущего

count = 0
numbers = [int(n) for n in input().split()]
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1
print(count)

# count = 0
# numbers = input().split()
# for i in range(1, len(numbers)):
#     if int(numbers[i]) > int(numbers[i - 1]):
#         count += 1
# print(count)
