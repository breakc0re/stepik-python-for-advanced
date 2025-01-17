# Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные
# числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке.

# Примечание. Остаток 2 при делении на 5 должно давать само число, а не его куб.


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def sortnums(function, items):
#     return items ** 3 if len(items) >= 3



# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# res = nums(filter, nums)
# print(res)

# a, b = int(input()), int(input())
#
# if a < b:
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             print(i, end=' ')
# else:
#     nums = []
#     for i in range(b + 1, a + 1):
#         if i % 2 != 0:
#             nums.append(i)
#     print(*sorted(nums, reverse=True))


# n = int(input())
# res = []
# for i in range(n):
#     number = int(input())
#     if number % 2 == 0:
#         res.append(number)
# print(sum(res) / len(res))


# n = int(input())
# numbers = []
# if len(str(abs(n))) == 3:
#     numbers.append(n)
# while n != 0:
#     n = int(input())
#     if len(str(abs(n))) == 3:
#         numbers.append(n)
# if len(numbers) == 0:
#     print('NO')
# else:
#     print(min(numbers))



# numbers = input().split()
#
# result = []
#
# for i in range(len(numbers)):
#
#     result.append(numbers[i])
#
# print(*result)


# numbers = input().split()
# numbers.append(numbers.pop(0))
# print(*numbers)


# n = int(input())
# total = 1
# result = []
# if 0 < n <= 30:
#     total *= n
#     result.append(n)
# while n != 0:
#     n = int(input())
#     if 0 < n <= 30:
#         total *= n
#         result.append(n)
# if len(result) == 0:
#     print(0)
# else:
#     print(total)


n = int(input())
h = (n // (60*60)) % 24
m = (n // 60) % 60
s = n % 60
if len(str(m)) == 1:
    print('{}:0{}:{}'.format(h, m, s))
else:
    print('{}:{}:{}'.format(h, m, s))