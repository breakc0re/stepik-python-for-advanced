# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
# 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
# 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
# 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#
# n = int(input())
#
# # new_numbers = [i % n == 0 for i in numbers]
# new_numbers = [i for i in numbers if i % n == 0]
#
#
# # for i in numbers:
# #     if i % n == 0:
# #         new_numbers.append(i)
# print(new_numbers)
from unittest import result


# total_temp = 0
# for i in range(5):
#     total_temp += float(input()[12:16])
# print(round((total_temp / 5), 1))


# text = input()
# print(text[:4] + ' ' + text[4:])
# print((x := input())[:4] + ' ' + x[4:])

# print((phrase := input()) in (text := input()))

# grades = input().split(' ')
#
# print(f'Средняя оценка {grades[0]}: {round((int(grades[1]) + int(grades[2]) + int(grades[3])) / 3, 1)}')
# # print(f'Средняя оценка {grades[0]}: {sum(grades) / 3}')


# email = input()[:-4].split('@', )[1]
# print(email[1])

# email = input()
# at = email.find('@')
# dot = email.find('.')
# print(email[at + 1:dot])

# print((email := input())[email.find('@') + 1:email.find('.')])

# n = int(input())  # Ввод целого положительного числа
#
# digit = True  # Флаг, указывающий на то, что число простое
#
# if n <= 1:
#     digit = False  # Число 1 и отрицательные числа не являются простыми
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             digit = False  # Число делится нацело на другое число, значит оно составное
#             break
#
# print(digit)  # Вывод результата проверки простоты числа

# m = int(input())
# from math import sqrt
# n = int(input())
# print('False' if n <= 1 else 'False' for i in range(2, int(sqrt(n) + 1)) if n % i == 0 else 'True')


# result = []
# for number in range(10, 100):
#     if number == ((number // 10 * number % 10) * 3):
#         result.append(number)
# print(result)


# numbers = [22, 9, 37, 44, 46, 69, 24, 100, 97, 57, 1, 6, 27, 96, 16, 82, 10, 95, 99, 78, 62, 50, 77, 86, 56, 40,
# 49, 32, 53, 76, 63, 67, 52, 0, 93, 84, 28, 8, 41, 79, 25, 21, 71, 43, 81, 72, 20, 90, 39, 75, 85, 14, 15, 60, 64,
# 5, 66, 4, 36, 98, 80, 12, 47, 91, 73, 45, 31, 65, 87, 74, 11, 34, 33, 18, 58, 23, 68, 94, 92, 17, 26, 88, 35, 13,
# 7, 42, 38, 19, 48, 29, 3, 59, 55, 51, 89, 2, 70, 83, 61, 54, 30]
#
# count = 0
#
# for i in range(1, len(numbers) - 1):
#     if numbers[i - 1] < numbers[i] > numbers[i + 1]:
#         count += 1
# print(count)

# k = int(input())
# vocabulary = {}
#
# for i in range(0, k):
#     ru, sp = input().split()
#     vocabulary[ru] = sp
#
# word = input()
# translation = vocabulary.get(word)
# print(translation)


# class Triangle:
#
#     def __init__(self, angle_1, angle_2, angle_3):
#         self.angle_1 = angle_1
#         self.angle_2 = angle_2
#         self.angle_3 = angle_3
#
#         if angle_1 > 0 and angle_2 > 0 and angle_3 > 0 and angle_1 + angle_2 + angle_3 == 180:
#             print("Triangle initialized")
#         else:
#             print("Initialization failed")
#
#
# angles = list(map(int, input().split()))
# triangle = Triangle(angles[0], angles[1], angles[2])
#


# import requests
# from bs4 import BeautifulSoup

###################################
# url = "https://stepik.org/media/attachments/lesson/209719/2.html"
# response = requests.get(url)
# html_content = response.text
#
#
# soup = BeautifulSoup(html_content, "html.parser")
#
#
# code_tags = soup.find_all("code")
#
#
# counter = {}
#
# for tag in code_tags:
#     code_string = tag.string
#     if code_string in counter:
#         counter[code_string] += 1
#     else:
#         counter[code_string] = 1
#
#
# max_count = max(counter.values())
# most_frequent_strings = [string for string, count in counter.items() if count == max_count]
#
#
# result = " ".join(sorted(most_frequent_strings))
# print(result)
###############################################
# import requests
# from bs4 import BeautifulSoup
#
# # Получение содержимого HTML-страницы
# url = "https://stepik.org/media/attachments/lesson/209723/3.html"
# response = requests.get(url)
# html_content = response.text
#
# # Парсинг HTML-страницы
# soup = BeautifulSoup(html_content, "html.parser")
#
# # Поиск таблицы
# table = soup.find("table")
#
# # Сумма чисел в таблице
# total_sum = 0
#
# # Обход строк таблицы
# for row in table.find_all():
#     # Обход ячеек в строке
#     for cell in row.find_all("td"):
#         # Получение текста из ячейки и преобразование в число
#         cell_text = cell.text.strip()
#         if cell_text.isdigit():
#             total_sum += int(cell_text)
#
# # Вывод суммы
# print(total_sum)

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')
#     print()


# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)
#
# print(maximum + minimum)


# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
#
# print(maximum + minimum)


# n = int(input())
# for i in range(n):
#     print([j for j in range(1, n + 1)])

# n = int(input())
# print(*[[i for i in range(1, n + 1)] for j in range(n)], sep='\n')


# grades = map(int, input().split())
# print('Сессия сдана!' if (2 not in grades or 1 not in grades) else 'На пересдаче')


# grades = list(map(int, input().split()))
# flag = False
# for i in grades:
#     if i >= 3:
#         flag = True
#     else:
#         flag = False
#         break
# if flag:
#     print('Сессия сдана!')
# else:
#     print('На пересдаче')

# N = int(input())
# A = [True] * N
# A[0] = A[1] = False
# for k in range(2, N):
#     if A[k]:
#         for m in range(2 * k, N, k):
#             A[m] = False
# for k in range(N):
#     print(k, '-', 'простое' if A[k] else 'составное')

# A = [4, 2, 5, 1, 3]
# N = len(A)
# for bypass in range(1, N):
#     for k in range(0, N - bypass):
#         if A[k] > A[k + 1]:
#             A[k], A[k + 1] = A[k + 1], A[k]
# print(A)

# def matryoshka(n):
#     if n == 1:
#         print('Матрёшечка')
#     else:
#         print('Верх матрёшки n=', n)
#         matryoshka(n - 1)
#         print('Низ матрёшки n=', n)

# import graphics as gr
#
# window = gr.GraphWin('Russian game', 600, 600)
# alpha = 0.2
#
#
# def fractal_rectangle(A, B, C, D, depth=10):
#     if depth < 1:
#         return
#     for M, N in (A, B), (B, C), (C, D), (D, A):
#         gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
#     A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
#     B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
#     C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
#     D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
#     fractal_rectangle(A1, B1, C1, D1, depth - 1)
#
#
# fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))

# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
#
# print(sum((min(my_dict), max(my_dict))))

# n = int(input())
#
# fib = [0, 1] + [0] * (n - 1)
# for i in range(2, n + 1):
#     fib[i] = fib[i - 1] + fib[i - 2]
#
#
# print(fib)

# import random
#
# num = random.randrange(10)
# print(num)

# import random
#
# n = int(input())    # количество попыток
# for i in range(n):
#     res = random.randrange(0, 2)
#     if res == 0:
#         print('Орел')
#     else:
#         print('Решка')

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
# my_dict = {key: [value for value in value if value <= 20] for key, value in my_dict.items()}
# print(my_dict)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# result = []
#
# for domain, usernames in sorted(emails.items()):
#     for username in sorted(usernames):
#         result.append((username + '@' + domain))
# print(*sorted(result), sep='\n')

# score = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
#          2: ['D', 'G'],
#          3: ['B', 'C', 'M', 'P'],
#          4: ['F', 'H', 'V', 'W', 'Y'],
#          5: ['K'],
#          8: ['J', 'X'],
#          10: ['Q', 'Z']}
#
# word = input().upper()
# total_score = 0
#
# for i in word:
#     for k, v in score.items():
#         if i in v:
#             total_score += k
# print(total_score)

# import random
#
#
# def generate_ip():
#     ip = []
#     for i in range(4):
#         sub_ip = random.randint(0, 256)
#         ip.append(sub_ip)
#     # print(ip[0])
#     return f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}'
#
# print(generate_ip())

# import random
#
# n = 10 ** 6
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if x ** 3 + y ** 4 + 2 >= 0 and 3*x + y**2 <= 2:
#         k += 1
#
# print((k/n)*s0)


# import random
# import time
# s = time.time()
# a = [1, 3, 5, 11, 7, 8, 2, 9, 4, 6, 10]
# while a != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
#     random.shuffle(a)
#     print(a)
# print(time.time() - s)


# from decimal import *
#
# num = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
#
# if num == 0:
#     print('YES')
# else:
#     print('NO')

# from fractions import Fraction
#
# num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
# num2 = Fraction('0.55')
# num3 = Fraction('1/9')
#
# print(num1, num2, num3, sep='\n')

# from fractions import Fraction
#
# num1 = Fraction(5, 1)        # 5/1 = 5
# num2 = Fraction(23, 23)      # 23/23 = 1
#
# print(num1, num2, sep='\n')

# k = int(input())
#
# peoples_list = [input().split() for _ in range(k)]
#
#
# def get_youngest(data):
#     name = ''
#     age = 200
#
#     for n, a in data:
#         a = int(a)
#         if a < age:
#             name = n
#             age = a
#     return name, age
#
#
# print(*get_youngest(peoples_list))

# values = tuple(map(int, input().split()))
#
#
# def mean(data):
#     return (*values, sum(data) / len(data))
#
#
# print(*mean(values))


# contacts = {
#     "Алиса": "+795006285923",
#     "Игорь": "+791234567890",
#     "Олег": "+790123456789",
#     "Елена": "+798765432109",
#     "Николай": "+785988877766",
#     "Анна": "+795977766655",
#     "Наташа": "+798877766655"
# }
#
# name = input()
#
# print(contacts.get(name))


# catalog = {
#     "яблоки": 10,
#     "груши": 5,
#     "бананы": 8,
#     "апельсины": 15,
#     "мандарины": 12,
#     "ананасы": 3
# }
#
# print('True' if input() in catalog else 'False')


# users = {
#     "JohnDoe": {
#         "email": "johndoe@example.com",
#         "phone": "+323456789",
#         "password": "pa$$w0rd"
#     },
#     "JaneSmith": {
#         "email": "janesmith@example.com",
#         "phone": "+987654321",
#         "password": "secret789"
#     },
#     "MikeJohnson": {
#         "email": "mikejohnson@example.com",
#         "phone": "+556447222",
#         "password": "qwerty123"
#     }
# }
#
# login, password = input().split()
#
# if login in users:
#     if password == users[login]['password']:
#         print('Доступ разрешен')
#     else:
#         print('Доступ запрещен')
# else:
#     print('Нет такого пользователя')


# events = {
#     "Завтрак": "07:30",
#     "Планирование": "09:00",
#     "Встреча с клиентом": "11:00",
#     "Обеденный перерыв": "13:00",
#     "Совещание": "15:00",
#     "Заказ продуктов": "17:00",
#     "Тренировка": "18:30",
#     "Ужин": "20:00"
# }
#
# res = [value for value in events.values()]
# print(*res, sep=', ')


# expenses = {
#     "Отель": 1000,
#     "Еда": 500,
#     "Транспорт": 300,
#     "Экскурсии": 200,
#     "Покупки": 400,
#     "Развлечения": 250,
#     "Экстренные расходы": 500
# }
#
# print(sum(expenses.values()))


# first_num, second_num = input().split()
# first_num, second_num = second_num, first_num
# print(first_num, second_num)


# foo = "REX"
# bar = "BIT"
# baz = "CAM"
#
# answer = baz[-1] + baz[-2] + bar[-1] + foo[0] + bar[1] + foo[-1]
# print(answer)


# kax = 100
# mar = kax // 7
# rep = mar % 5 / float(2)
#
# bat = kax / (rep + 1)
#
# print('%.2f' % bat)


# for i in range(len(word)):
#     new_word = word[-i:] + word[:-i]
#     print(new_word)


# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
#
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
#
# print(total)
# print(product)


# def high_order_function(func):
#     return func(10)
#
#
# def square(x):
#     return x**2
#
#
# def minus_one(x):
#     return x - 1
#
#
# num1 = high_order_function(square)
# num2 = high_order_function(minus_one)
#
# print(num1*num2)


# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']
#
# words_len = map(len, words)
# print(list(words_len))
# print(max(words_len))
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
#
# print(var1 + var2)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# result = ([round(i, 2) for i in numbers])
# print(*result, sep='\n')


# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
# for k, v in countries.items():
#     if city in v:
#         country = k
#         print(f'INFO: {city} is a city in {country}')
#         break
# else:
#     print(f'ERROR: Country for {city} not found')


# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17"
# }
#
#
# for key, value in user.items():
#     if key == 'password':
#         user.pop(key)
#         user['secret'] = value
#         # user[key] = value
#         break
#
# for key, value in user.items():
#     if key == 'last_name':
#         user.pop(key)
#         user['surname'] = value
#         break
#
# print(user)

# dictionary = {list[n] : dictionary}


# nums = [int(i) for i in input().split()]
# d = nums.pop()
# while nums:
#     d = {nums.pop(): d}
#
# print(d)

# s = input()
# d = {}
#
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# words = {}
# while True:
#     s = input()
#     if s in words:
#         print(f'Слово {s}, переводится как {words[s]}')
#     else:
#         print(f'Введите перевод слова {s}')
#         words[s] = input()


# def create_matrix(size=3, up_fill=0, down_fill=0):
#     matrix = []
#     for i in range(size):
#         row = []
#         for j in range(size):
#             if i == j:
#                 row.append(i + 1)
#             elif i < j:
#                 row.append(up_fill)
#             else:
#                 row.append(down_fill)
#         matrix.append(row)
#     return matrix
#
# assert create_matrix() == [[1, 0, 0],
#                            [0, 2, 0],
#                            [0, 0, 3]]
# assert create_matrix(4) == [[1, 0, 0, 0],
#                             [0, 2, 0, 0],
#                             [0, 0, 3, 0],
#                             [0, 0, 0, 4]]
# assert create_matrix(up_fill=7) == [[1, 7, 7],
#                                     [0, 2, 7],
#                                     [0, 0, 3]]
# assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
#                                                  [9, 2, 7],
#                                                  [9, 9, 3]]
# assert create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
#                                                          [9, 2, 7, 7],
#                                                          [9, 9, 3, 7],
#                                                          [9, 9, 9, 4]]


# def count_args(*args):
#     return len(args)
#
# print(count_args(1, 2, 3))
# print(count_args(1, 3))
# print(count_args(2))
# print(count_args())


# def check_sum(n):
#     n = map(int, input().split())
#     if sum(n) < 50:
#         return 'not enough'
#     else:
#         return 'verification passed'

# def check_sum(*args):
#     res = [int(i) for i in args]
#     if sum(res) < 50:
#         print('not enough')
#     else:
#         print('verification passed')
#
#
# mas = input().split()
#
# print(check_sum(*mas))


# def multiply(*args: int) -> int:
#     sum = 1
#     for i in args:
#         sum *= i
#     return sum
#
#
# assert multiply(1, 2, 3) == 6
# assert multiply(1, 3) == 3
# assert multiply(2) == 2
# assert multiply() == 1
# print('All done!')


# def only_one_positive(*args: int) -> bool:
#     res = 0
#     for i in args:
#         if i > 0:
#             res += 1
#
#     if res == 1:
#         return True
#     else:
#         return False
#
#
# assert only_one_positive(1, 2) is False
# assert only_one_positive(-1, 0, -3, 5, -3) is True
# assert only_one_positive() is False


# def print_goods(*args):
#     lst = []
#     res = []
#     for i in args:
#         if isinstance(i, str) and len(i) != 0:
#             lst.append(i)
#
#     for i in range(1, len(lst) + 1):
#         res.append(f'{i}. {lst[i - 1]}')
#
#     if len(res) == 0:
#         print('Нет товаров')
#     else:
#         print(*res, sep='\n')
#
#
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# print_goods([], {}, 1, 2)


# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# info_kwargs(first_name="John", last_name="Doe", age=33)


# def create_actor(name='Райан', surname='Рейнольдс', age=46, **kwargs):
#     d = dict()
#     d.setdefault('name', name)
#     d.setdefault('surname', surname)
#     d.setdefault('age', age)
#     print(d | kwargs)
#     return d | kwargs
#
#
# assert create_actor() == {
#     'name': 'Райан',
#     'surname': 'Рейнольдс',
#     'age': 46, }
# assert create_actor(height=190, movies=['Дедпул', 'Главный герой']) == {
#     'name': 'Райан',
#     'surname': 'Рейнольдс',
#     'age': 46,
#     'height': 190,
#     'movies': ['Дедпул', 'Главный герой']}
# assert create_actor(name='Jack', age=20) == {
#     'name': 'Jack',
#     'surname': 'Рейнольдс',
#     'age': 20, }


# def print_from(n: int) -> None:
#     if n > 0:
#         print(n + 1)
#         print_from(n + 1)


# def print_to(n: int) -> None:
#     for i in range(1, n + 1):
#         print(i)
#
#
# print(print_to(10))


# def print_to(n: int) -> None:
#     "A sequence of integers"
#     if n > 0:
#         print_to(n-1)
#         print(n)
#
# print_to(10)


# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]
#
# s = input()
# print(rec(s))


# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1 / power(x, -n)
#     if n % 2 == 0:
#         return power(x, n // 2) * power(x, n // 2)
#     else:
#         return power(x, n - 1) * x
#
#
# x = int(input())
# n = int(input())
# print(power(x, n))


# a = [1, [3, [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]
#
# def rec(spisok, level=1):
#     print(*spisok, 'level=', level)
#     for i in spisok:
#         if type(i) == list:
#             rec(i, level + 1)
#
#
# rec(a)


# обход файлов
# import os
#
# path = 'C:\\Movies'
# # print(os.listdir(path))
# # for i in os.listdir(path):
# #     print(i, type(i), path+'\\' + i, os.path.isdir(path+'\\' + i))
# #     # print(i, type(i), path+'\\' + i, os.path.isfile(path+'\\' + i))
#
#
# def obhodFile(path, level=1):
#     print('Level=', level, 'Content:', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\' + i):
#             print('Спускаемся', path + '\\' + i)
#             obhodFile(path + '\\' + i, level + 1)
#             print('Возвращаемся в', path)
#
#
# obhodFile(path)


# starts_with = lambda x: True if x.startswith('W') else False
# print(starts_with('World'))


# sq = lambda x, y: x ** 2 + y ** 2


# average = lambda *args: sum(args) / len(args)
# print(average(2, 3, 4))


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# subject_marks.sort(key=lambda x: x[1])
# for i in subject_marks:
#     print(*i)


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# subject_marks.sort(key=lambda x: x[1], reverse=True)
# for i in subject_marks:
#     print(*i)


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# subject_marks.sort(key=lambda x: (-x[1], x[0]))
# for i in subject_marks:
#     print(*i)


# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# for i in sorted(models, key=lambda x: x['color']):
#     print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")

# res = []
# while (n := input()) != 'конец':
#     res.append(n.split(':'))
# for i in sorted(res, key=lambda x: int(x[1]), reverse=True):
#     print(i[0])


# n = int(input())
# res = {}
# for i in range(n):
#     actor = input()
#     if actor not in res:
#         res[actor] = 1
#     else:
#         res[actor] += 1
#
# minimum = min(res.items(), key=lambda x: x[1])
# maximum = max(res.items(), key=lambda x: x[1])
#
# if len(res) >= 1:
#     print(*maximum, sep=', ')
#     print(*minimum, sep=', ')


# phone_book = {}
# n = int(input())
# for i in range(n):
#     phone, name = input().split()
#     if name not in phone_book:
#         phone_book[name] = []
#     phone_book[name].append(phone)
# print(phone_book)
# m = int(input())
# for j in range(m):
#     contact = input()
#     if contact in phone_book:
#         print(" ".join(phone_book[contact]))
#     else:
#         print("Неизвестный номер")


# birthdays = {}
# n = int(input())
# for i in range(n):
#     name, day, month = input().split()
#     if month not in birthdays:
#         birthdays[month] = []
#     birthdays[month].append(name)
#
# m = int(input())
# for j in range(m):
#     contact = input()
#     if contact in birthdays:
#         print(*sorted(birthdays.get(contact), key=lambda x: x[0]))
#     else:
#         print("Нет данных")


# res = {}
# while True:
#     n = input()
#     if n == 'конец':
#         break
#
#     name, rating = n.split(', ')
#     if name not in res:
#         res[name] = {'sum': 0, 'count': 0}
#     res[name]['sum'] += int(rating)
#     res[name]['count'] += 1
#
# total_ratings = []
# for name, data in res.items():
#     avg = data['sum'] / data['count']
#     total_ratings.append((name, avg))
#
# for i in sorted(total_ratings, key=lambda x: (-x[1], x[0])):
#     print(f'{i[0]} {i[1]}')


# comments = {
#     'Дили': set(),
#     'Вили': set(),
#     'Били': set(),
# }
#
# a = input()
# while a != 'конец':
#     name, commentator = a.split(': ')
#     comments[name].add(commentator)
#     a = input()
# print(comments)
# for k, v in sorted(comments.items(), key=lambda item: -len(item[1])):
#     print(f'Количество уникальных комментаторов у {k} - {len(v)}')


# def calculate(x, y, operation='a'):
#
#     def addition():
#         print(float(x + y))
#
#     def subtraction():
#         print(float(x - y))
#
#     def division():
#         if y == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(float(x / y))
#
#     def multiplication():
#         print(float(x * y))
#
#     if operation == 'a':
#         addition()
#     elif operation == 's':
#         subtraction()
#     elif operation == 'd':
#         division()
#     elif operation == 'm':
#         multiplication()
#     else:
#         print('Ошибка. Данной операции не существует')


# calculate(2, 5)
# calculate(2.2, 15, 'a')
# calculate(22, 15, 's')
# calculate(2, 3.2, 'm')
# calculate(10, 0.4, 'd')
# calculate(10, 0, 'd')


# def create_accumulator(value=0):
#     counter = value
#
#     def inner(number):
#         nonlocal counter
#         counter += number
#         return counter
#
#     return inner
#
# summator_1 = create_accumulator(100)
# print(summator_1(1)) # печатает 101
# print(summator_1(5)) # печатает 106
# print(summator_1(2)) # печатает 108
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7


# def multiply(value):
#     def inner(number):
#         return value * number
#     return inner
#
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45


# def decor(func):
#     def inner(*args, **kwargs):
#         print("very hard")
#         func(*args, **kwargs)
#         print("decorator is difficult")
#
#     return inner
#
#
# @decor
# def my_func(x):
#     print(f"my grade for decorator: {x}")
#
#
# my_func(5)


# from string import ascii_lowercase, ascii_uppercase, punctuation
#
# print(punctuation, ascii_uppercase, ascii_lowercase, sep='\n')
# # print(ascii_uppercase)
# # print(ascii_lowercase)


# def file_read(file_name: str) -> None:
#     file = open(file_name, 'r', encoding='utf-8')
#     print(file.read())
#     file.close()
#
#
# file_read('lol.txt')


# def file_n_lines(file_name: str, n: int) -> None:
#     file = open(file_name, 'r', encoding='utf-8')
#     for row in range(n):
#         print(file.readline().strip('\n'))
#     file.close()
#
# file_n_lines('hello.txt', 3)


# def create_file_with_numbers(n: int) -> None:
#     file = open(f'range_{n}.txt', 'w', encoding='utf-8')
#     for num in range(1, n + 1):
#         file.write(str(num) + '\n')
#     file.close()
#
# create_file_with_numbers(5)


# def longest_word_in_file(file_name: str) -> str:
#     f = open(file_name, 'r', encoding='utf-8')
#     max_word = ''
#     for line in f:
#         words = line.split()
#         for word in words:
#             new_word = remove_punct(word)
#             if len(new_word) >= len(max_word):
#                     max_word = new_word
#     return max_word
#
# def remove_punct(word):
#     from string import punctuation
#     for punc in punctuation:
#         if punc in word:
#             word = word.replace(punc, '')
#     return word
#
#
# print(longest_word_in_file('hello.txt'))


# def check_file(file_name: str) -> str:
#     count = 0
#     summ = 0
#     numbers = list(map(int, open("numbers.txt").read().split()))
#     for i in numbers:
#         if len(str(i)) == 3:
#             count += 1
#         elif len(str(i)) == 2:
#             summ += i
#     print(count)
#     print(summ)
# check_file('numbers.txt')


# def find_lines_len_more_6(file_name:str) -> int:
#     with open(file_name, 'r', encoding='utf-8') as f:
#         count = 0
#         res = [str(i) for i in f.read().splitlines()]
#         for line in res:
#             if len(line) > 6:
#                 count += 1
#     return count
#
# find_lines_len_more_6('hello.txt')


# with open('words.txt', 'r', encoding='utf-8') as f:
#     res = []
#     lst = [word.upper() for i in f.read().splitlines() for word in i.split(' ')]
#     for i in lst:
#         if i not in res and i.endswith('ЕЯ'):
#             res.append(i)
#     print(*(sorted(res, key=lambda x: (len(x), x[0]))), sep='\n')


# import json
#
# dictt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#
# json_data = json.dumps(dictt, indent=3)
# print(json_data)


# import json
# maximum = 0
# max_name = ''
# max_lastname = ''
# with open('manager_sales.json') as file:
#     data = json.load(file)
#
#     for element in data:
#         name = element['manager']['first_name']
#         lastname = element['manager']['last_name']
#         total = 0
#         for car in element['cars']:
#             total += car['price']
#         if total > maximum:
#             maximum = total
#             max_name = name
#             max_lastname = lastname
#     print(max_name, max_lastname, maximum)


# import json
# total = 0
# max_group = None
# # max_name = ''
# # max_lastname = ''
# with open('group_people.json') as file:
#     data = json.load(file)
#
#     for group in data:
#         count = 0
#         id_group = group['id_group']
#         for person in group['people']:
#             if person['gender'] == 'Female' and person['year'] > 1977:
#                 count += 1
#         if count > total:
#             total = count
#             max_group = id_group
#     print(max_group, total)


# import json
#
# with open('Alphabet.json', 'r') as file:
#     jsn = json.load(file)
# with open('Abracadabra__1_.txt', 'r', encoding='utf-8') as file:
#     txt = file.read()
#
# print(''.join(jsn[i] if i in jsn else i for i in txt))


# import json
#
# people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, {"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", "country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": "Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", "country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": "Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", "age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, {"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": "Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": "Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", "country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": "Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'
#
# data = json.loads(people)
#
# res = sorted(data, key=lambda x: (x['age'], x['name']))
# for i in res:
#     print(f"{i['name']}, {i['country']}, {int(i['age'])}")


# import json
#
#
# json_string = """
# {
#     "customers": [
#         {
#             "userid": 123456,
#             "username": "Allie Hsu",
#             "phone": [
#                 "000-001-0002",
#                 "000-002-0002"
#             ],
#             "is_vip": true
#         },
#         [{
#             "userid": 223678,
#             "username": "Donald Duck",
#             "phone": null,
#             "is_vip": false
#         }]
#     ]
# }
# """
#
# data = json.loads(json_string)
# print(data['customers'][0]['username'])


# # Создайте генератор
# from_10_to_20 = (i for i in range(10, 21))
#
# # Распечатайте три первых значения
# print(next(from_10_to_20))
# print(next(from_10_to_20))
# print(next(from_10_to_20))
#
# # выведите все оставшиеся
# for value in from_10_to_20:
#     print(value)


# day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days = ((date, day[(date + 4) % 7]) for date in range(1, 78))
# print(*days, sep='\n')


# def gen_squares(n):
#     squares = (j ** 2 for j in range(1, n + 1))
#     for i in squares:
#         yield i


# def gen_fibonacci_numbers(n):
#     a, b = 1, 1
#     count = 0
#
#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1
#
#
# # Пример использования
# for i in gen_fibonacci_numbers(5):
#     print(i)
#
# for i in gen_fibonacci_numbers(10):
#     print(i)

# # Копия range
# # Ваша задача создать функцию-генератор my_range_gen, которая копирует работу range.
# def my_range_gen(*args):
#     if len(args) == 1:  # Если передан один параметр (stop)
#         start = 0
#         stop = args[0]
#         step = 1
#     elif len(args) == 2:  # Если переданы два параметра (start, stop)
#         start = args[0]
#         stop = args[1]
#         step = 1
#     elif len(args) == 3:  # Если переданы три параметра (start, stop, step)
#         start = args[0]
#         stop = args[1]
#         step = args[2]
#         if step == 0:  # Если шаг равен 0, прекращаем генерацию
#             return
#         if (start < stop and step < 0) or (start > stop and step > 0):
#             return
#
#     current = start
#     while (step > 0 and current < stop) or (step < 0 and current > stop):
#         yield current
#         current += step


# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609, 221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278, 118, -462, -671, 78, -69, -568, -228, -445, -47, -565]
# strings = list(map(str, numbers))
# print(strings)


# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609, 221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278, 118, -462, -671, 78, -69, -568, -228, -445, -47, -565]
# print(increase_3 := list(map(lambda x: x * 3, numbers)))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x ** 2, numbers)))
# print(list(map(lambda x: x ** 3, numbers)))


# def from_hex_to_rgb(color: str) -> tuple:
#     red = int(color[1:3], 16)
#     green = int(color[3:5], 16)
#     blue = int(color[5:7], 16)
#     return red, green, blue
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
#           '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
#           '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
#           '#7CFC00', '#7FFF00', '#ADFF2F']
#
# for red, green, blue in map(from_hex_to_rgb, colors):
#     print(f"Red={red}, Green={green}, Blue={blue}")


# print(list(map(lambda x: (x.upper(), x.lower()), input().split())))


# names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
#          ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
#          ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
#          ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
#          ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
#          ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
#          ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
#          ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
#          ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
#          ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
#          ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
#          ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
#          ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
#          ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
#          ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]
#
# new_names = list(map(lambda x: (x[0] + ' ' + x[1]), names))
# print(new_names)


# persons = [
#     {
#         'birthday': '1983-10-25',
#         'job': 'Field seismologist',
#         'name': 'Andrew Hernandez',
#         'phone': '680-436-8521x3468'
#     },
#     {
#         'birthday': '1993-10-03',
#         'job': 'Pathologist',
#         'name': 'Paul Harmon',
#         'phone': '602.518.4130'
#     },
#     {
#         'birthday': '2002-06-11',
#         'job': 'Designer, multimedia',
#         'name': 'Gregory Flores',
#         'phone': '691-498-5303x079'
#     },
#     {
#         'birthday': '2006-11-28',
#         'job': 'Print production planner',
#         'name': 'Jodi Garcia',
#         'phone': '(471)195-7189'},
#     {
#         'birthday': '2019-12-05',
#         'job': 'Warehouse manager',
#         'name': 'Elizabeth Cannon',
#         'phone': '001-098-434-5950x276'
#     },
#     {
#         'birthday': '1984-06-12',
#         'job': 'Visual merchandiser',
#         'name': 'Troy Lucas',
#         'phone': '+1-018-070-2288x18433'
#     },
#     {
#         'birthday': '1993-09-14',
#         'job': 'International aid/development worker',
#         'name': 'Laurie Sandoval',
#         'phone': '2930693269'
#     },
#     {
#         'birthday': '1999-05-25',
#         'job': 'Editor, film/video',
#         'name': 'Jack Clark',
#         'phone': '8643048473'
#     },
#     {
#         'birthday': '1985-09-11',
#         'job': 'Magazine journalist',
#         'name': 'Kimberly Johnson',
#         'phone': '+1-583-428-7663'
#     },
#     {
#         'birthday': '1990-10-07',
#         'job': 'Museum/gallery curator',
#         'name': 'Austin Liu PhD',
#         'phone': '714-879-5250'
#     }
# ]
#
# # phones = list(map(lambda x: x['phone'], persons))
# print(phones := list(map(lambda x: x['phone'], persons)))


# list_x = [25, 48, 23, 13, -18, -10, -3, 16, 2, -12, 20, -14, 14, 45, 41, 6, 11, 15, 22,
#           -14, -11, 41, 15, 48, 47, 41, -8, 1, 4, 1, 40, 27, -11, -2, -14, -15, 35, 4,
#           49, 4, 5, 13, 50, 35, -3, 3, 30, -11, 7, 12]
#
# list_y = [-9, 17, 41, 47, -5, -10, -5, 13, 31, -11, 37, 9, 46, 27, -1, 36, 32, 23, -12,
#           38, 8, 9, 17, 16, 29, -4, 4, 2, 1, 46, 6, 49, -16, 21, -19, -10, 15, -13, 20,
#           13, -18, 21, -17, 21, 10, 5, 38, -1, 18, 22]
#
# list_w = [9, -26, 3, 21, 48, -14, 43, -4, -16, 16, 41, 43, -27, -9, 10, -10, 4, -2, 1,
#           7, 30, -29, 11, 17, 31, 31, -26, 38, 38, -17, 35, 17, 35, 10, -25, 42, -30,
#           -10, -20, 20, 15, 0, 29, -30, -21, -13, -27, -21, -18, -26]
#
# print(list(map(lambda x, y, w: (x ** 2) - (x * y * w) + (w ** 4), list_x, list_y, list_w)))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 == 0, numbers)))


# numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26, -46, -97, -28, 36, 7, 52, 56, -96, -69, 67, 76, 16, 36, 38, 74, 11, -87, 69, 69, -69, -61, 92, 67, -45, -26, 94, 38, 27, -26, 10, 55, 28, -81, 53, -75, -32, -83, 38, 83, -40, -51, 88, 28, 76, 25, 84, -79, -69, -65, 6, 12, 81, -58, -92, 44, -41, 60, -14, -65, 7, 64, -40, -25, -91, -23, -19, -40, -4, 36, 38, 28, -27, -28, 72, 47, -95, 47, 10, 31, 62, -75, 22, -34, 44, -62, -30, -41, 19, -13, 30, -11, -54, -46, -80, -57, -60, 72, -49, 84, 5, 66, 62, -35, 69, 23, 41, -15, 75, -53, 94, -76, -28, -41, -17, 71, 67, -50, 18, 65, -16, -27, -88, 21, -42, 58, 85, 36, 9, -72, -26, -73, -1, 41, -87, 85, 5, -92, -60, -33, 33, -74, 17, 47, -38, -95, -39, 64, 85, -27, -42, -91, -39, -15, -75, 78, -54, 26, -10, -3, 89, -11, -71, -85, 63, 9, -59, 72, 27, 40, 99, -9, 77, 64, -39, -28, 73, -50, -80, -74, 52, 26, 53, -18, 22, 70, 85, 1, -90, 53, -19, -80, -14, -29, -64, -21, 23, 99, 15, -52, 66, 30, 82, -81, -30, -68, 30, -25, -63, 33, 1, 0, 84, 18, -35, 31, -34, 10, 48, -37, -41, -94, -1, -14, -87, -37, -6, 48, 38, 33, -13, 71, -81, 45, -63, 52, -35, 34, -88, -82, -7, -92, -22, 96, -28, 0, 21, 74, -28, 81, 81, 44, -16, 17, -95, 18, -73, 15, -61, 6, -43, -67, -31, -61, -72, -66, 60, 67, -13, 47, 29, 44, -93, 55, -13, -23, 74, 79, 32, -20, 33, 17, -48, 7, 24, 19, 89, -60, 34, 81, 18, -39, 56, 10, -32, 46, -33, -75, -99, -37, -23, 59, -33, -1, 75, -65, 92, 80, 51, -59, -28, -22, -47, -1, 28, -85, 1, 23, -15, -66, -97, -25, 7, 17, -87, -60, 14, -70, 88, 20, 40, -89, 38, -41, -97, 76, 80, 43, 22, -72, -38, 47, -2, 12, 58, -91, 82, -98, 50, 15, -33, -56, 69, -27, 94, -90, 92, -71, -73, -71, -78, 22, -86, -48, 10, 46, 19, 68, -23, 52, -42, 74, 44, 89, -71, 93, 43, -86, 79, 3, -56, 14, 41, 15, -37, 77, -9, 36, 51, -89, 1, 37, 82, 27, 72, -92, 91, 94, 71, -81, -49, -42, 26, 57, -30, -40, 86, -77, -85, 1, 71, 16, 73, -82, 26, -90, 72, 14, -65, -55, 34, 45, 66, -64, -40, 92, 42, -78, -22, 53, -18, -41, -75, 10, -59, -55, 8, -90, -3, -65, 43, -49, -86, -96, 69, 48, 27, -48, -42, -34, -6, 7, 50, -55, -65, 79, 30, 16, -21, -98, -73, -25, -20, -51, 20, 17, -91, 34, 96, 12, 13, -58, -73, -82, 19, -48, -61, 57, 96, 74, 34, -63, 38, -27, -12, -24, 94, -25, -10, -41, 53, -13, 16, -21, 24, 96, 95, 58, 83, 10, 42, -11, -33, 10, 38, -6, -66, -40, -36, -99, -55, 37, -81, -93, 67, -77, -3, 77, 25, 38, -16, 21, -82, 77, 95, 73, 9, 94, -27, -21, -33, -90, 31, 98, 28, -63, 75, 53, -17, -1, 6, 51, 11, -92, 30, -24, 12, 47, -75, -15, -63, 57, 3, 37, -82, -28, -26, -3, -30, -90, -45, 20, -41, 72, -42, 15, -3, 92, 57, -1, 40, -65, 88, 28, -76, 52, -63, -51, 59, 69, -39, -47, -1, -18, -57, 68, 77, 66, 62, -71, 31, -50, 61, 88, 98, 5, 98, -57, -46, 2, 90, 43, 67, 76, -81, -57, 77, 25, -66, -81, -92, -76, 72, 14, 59, 52, 36, 20, -2, 92, 58, 36, -34, 94, -74, 42, -56, 96, -81, 69, -83, 71, -13, -13, 56, 86, -29, 58, -17, 65, 70, 74, 28, 8, 91, 51, 79, -57, -86, 5, -37, -67, -28, 56, 65, -90, 97, -20, 81, -85, -45, 46, -74, 76, -75, -7, 74, 82, 56, 14, -43, 20, -48, -99, 19, -39, -66, 44, -75, 24, -5, -70, 85, -12, 20, -85, -69, -26, -57, 28, -96, 42, -56, 13, 80, -48, 59, 11, -30, 4, -96, 58, 41, -2, -84, -51, 52, -69, 37, 60, -12, 48, -5, -48, 29, -62, 42, 15, 16, 65, 60, 43, -53, 4, 50, -21, 1, -21, -42, -57, -21, -50, -67, 77, -22, -5, 59, -67, 86, -77, 39, -67, 41, 83, -21, 33, 73, 55, 80, 93, 44, -71, 38, -93, 4, 83, -52, 75, -51, 1, -11, -45, 56, 81, 84, 70, 23, -36, -63, 69, 1, 86, -21, 53, -85, 70, -89, -31, -10, -94, -76, -17, -21, -60, 49, -22, -48, 67, 21, 18, 89, 20, 73, -43, -17, -52, 36, -21, 6, -37, -98, 94, 56, 31, 99, 86, 65, -19, -67, 46, 20, -29, -88, -54, 88, -12, -69, 17, 83, -94, 21, 59, -99, 70, -54, -35, 2, 58, 93, 1, -35, -44, 47, 40, 55, 10, -15, -96, -42, 10, -83, -82, -26, 48, 78, -72, 56, -99, -36, 25, 76, -3, -95, -38, -24, 96, 82, 7, 84, 46, 8, 93, -52, -86, 87, -85, -81, 52, -67, 52, -45, -93, -69, 60, -83, -20, -14, 80, -36, 62, -78, 3, -61, 51, 48, 73, 92, -65, 71, -86, 8, -14, 82, 58, -58, -21, 62, -38, 16, 20, -80, -78, 19, 19, 93, -83, 2, 71, 85, 71, -4, 81, 4, 90, 73, 21, -3, -55, 49, 66, -4, -6, 42, 76, -3, -94, 49, 55, -53, 12, 1, -25, 56, 93, -68, -21, 15, -13, 35, 71, -68, 34, -44, 48, 97, 51, 32, 87, 27, -85, -41, -27, 54, -91, -99, 83, -44, 70, -87, -76, 49, 99, 38, 15, 75, -54, -59, 22, 80, 49, -63, 8, -46, 97, -4, -92, -47, -20]
#
# negative = len(list(filter(lambda x: x < 0, numbers)))
# zero = len(list(filter(lambda x: x == 0, numbers)))
# positive = len(list(filter(lambda x: x > 0, numbers)))
# print(negative, zero, positive)


# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# print(*sorted(list(filter(lambda x: len(x) == 4 or x.startswith('S'), days))), sep='\n')


# employees = [
#     'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
#     'Leonti', 'Daniil', 'Mishka', 'Lidochka',
#     'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
# ]
#
# identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]
#
# print(employees_data := dict(zip(sorted(identifiers), (sorted(employees)))))


# def zip_with_function(a, func):
#     return list(map(lambda args: func(*args), zip(*a)))
#     # Напишите определение функции zip_with_function
#
# def combine_strings(a: str, b: str) -> str:
#     return a + b
#
# def get_sum_two_numbers(a: int, b: int) -> int:
#     return a + b
#
# def get_sum_three_numbers(a: int, b: int, c: int) -> int:
#     return a + b + c
#
# assert zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers) == [4, 7, 12]
# assert zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers) == [40, 20]
# assert zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers) == [10, 15, 20]
# assert zip_with_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]], get_sum_three_numbers) == [12, 15, 18]
# assert zip_with_function([["a", "b"], ["1", "2"]], combine_strings) == ['a1', 'b2']


# def count_strings(*args):
#     res = []
#     for i in args:
#         if isinstance(i, str):
#             res.append(i)
#     return len(res)
#
# print(count_strings(1, 2, 'hello', [2, 3, 4], True))
# print(count_strings('am', 'world', 'hello', 'is'))
# print(count_strings())
# print(count_strings(True, False))


# def find_keys(**kwargs):
#     res = []
#     for k, v in kwargs.items():
#         if isinstance(v, (list, tuple)):
#             res.append(k)
#     return sorted(res, key=lambda x: x.lower())
#
#
# print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
#
# print(find_keys(name='Bruce', surname='Wayne'))
#
# print(find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)))


# print(all(['a' in i for i in input().lower().split()]))


# print(any([i.endswith('ought') for i in input().lower().split()]))


# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# i = j = 0
# c = []
# while i < n and j < m:
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1
# while i < n:
#     c.append(a[i])
#     i += 1
# while j < m:
#     c.append(b[j])
#     j += 1
# print(*c)


# n = int(input())
# boys = list(map(int, input().split()))
#
# m = int(input())
# girls = list(map(int, input().split()))
#
# boys.sort()
# girls.sort()
# i = 0
# j = 0
# count = 0
# while i < n and j < m:
#     if abs(boys[i] - girls[j]) <= 1:
#         count += 1
#         i += 1
#         j += 1
#     elif boys[i] < girls[j]:
#         i += 1
#     else:
#         j += 1
# print(count)


# n = map(int, input().split())
# for i in n:
#     print('*' * i)

# count = 0
# n = int(input())
# for p in range(n + 1, 2 * n):
#     if p % 2 == 0 and p != 2 or p == 1:
#         continue
#     d = 3
#     is_plain = True
#     while d * d <= p:
#         if p % d == 0:
#             is_plain = False
#             break
#         d += 2
#     if is_plain:
#         count += 1
# print(count)


# def bubble_sort(arr):
#     n = len(arr)
#     swaps = 0
#
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swaps += 1
#                 swapped = True
#
#         if not swapped:
#             break
#
#     return arr, swaps
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# sorted_arr, num_swaps = bubble_sort(arr)
# print(' '.join(map(str, sorted_arr)))
# print(num_swaps)


# n, m = map(int, input().split())
# count = 0
# a = 0
# while a ** 2 <= n:
#     b = n - a ** 2
#     if b >= 0 and a + b ** 2 == m:
#         count += 1
#     a += 1
# print(count)


# n = int(input())
# a = []
# sum = 0
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(n):
#         if a[i] == a[j]:
#             sum += a[i][j]
# print(sum)


# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         print(a[j][i], end=' ')
#     print()


# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(m - 1, -1, -1):
#         print(a[i][j], end=' ')
#     print()


# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N - 1, -1, -1):
#     for j in range(M):
#         print(matrix[i][j], end=" ")
#     print()

# a = []
# for i in range(6):
#     a.append(i)
# print(*[i for i in range(6)], sep=' + ')


# for i in range(1, 6):
#     if i == 1 or i == 3 or i == 5:
#         print(input())


# n, m = int(input()), int(input())
# print(*['*' * m for i in range(n)], sep='\n')

# a, b, c, d = [int(input()) for i in range(4)]
# print(a * b + c * d)


# print(sum([i for i in range(1, int(input()) + 1)]))


# a, b, c, d = [float(input()) for i in range(4)]
# print(sum((a, b, c, d)) / 4)


# a, b, c = 7, 2, 10
# print(min(max(a, b), max(a, c), max(b, c)))

# a, b, c = [int(input()) for i in range(3)]
# print('YES' if a <= c <= b else 'NO')


# n = int(input())
# if n == 0:
#     print('зеленый')
# elif 1 <= n <= 10:
#     if n % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= n <= 18:
#     if n % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif 19 <= n <= 28:
#     if n % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= n <= 36:
#     if n % 2 == 0:
#         print('красный')
#     else:
#         print('черный')


# from math import ceil
# n, m = map(int, input().split())
#
# print(ceil((n + m) / 20))


# a, b = [int(input()) for i in range(2)]
# print(float(a * 2 + b * 2))


# number = input().split('.')
# # print(True if int(number[0]) % 3 == 0 else False)
# print(bool(int(number[0]) % 3 == 0))


# print((text := input())[0] + text[-1])


# word_1, word_2 = input().split()
# res1 = []
# res2 = []
# for i in range(len(word_1)):
#     if i % 2 != 0:
#         res1.append(word_1[i])
# for j in range(len(word_2)):
#     if j % 2 != 0:
#         res2.append(word_2[j])
# print(res1 == res2)


# word_1, word_2 = input().split()
# print(word_1[1:len(word_2):2] == word_2[1::2])

# text = 'My best friend is Python!'
# text = text.replace(' ', "'", 1).replace(' ', '"')
# print(text)


# number = input().replace('+7', '8').replace('-', '')
# lst = list(number)
# print(*lst, sep='')


# ticket = input()
# first_half = sum([int(i) for i in ticket[:3]])
# second_half = sum([int(i) for i in ticket[3::]])
# print('ДА' if first_half == second_half else 'НЕТ')


# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# note = map(int, input().split())
# res = []
# for i in note:
#     if m[i - 1] == 'до' or m[i - 1] == 'фа':
#         res.append('#' + m[i - 1])
#     else:
#         res.append(m[i - 1])
# print(*res)


# n = int(input())
# s = 2
# total = 1
# while s <= n:
#     total += 1/s
#     s += 1
# print(round(total, 3))


# summ = 0
# n = int(input())
# while n != 0:
#     summ += n % 10
#     print(summ)
#     n = n // 10
# print(summ)


# n = int(input())
# i = 0
# sum = [1, 1]
# while i != n - 2:
#     sum.append(sum[i] + sum[i + 1])
#     i += 1
# print(*sum)


# n = int(input())
# cells = 1
#
# while n >= 3:
#     cells *= 2
#     n -= 3
#
# print(cells)


# n = int(input())
# vklad = 1000
# while n > 0:
#     vklad_v_god = vklad + (vklad / 100 * 5)
#     vklad = vklad_v_god
#     n -= 1
# print(round(vklad, 2))


# n, m = map(int, input().split())
# result = ""
#
# while n <= m:
#     if n % 2 != 0:
#         result += str(n) + " "
#     n += 1
#
# print(result)


# p = [0] * 10
# cnt = 0
# while cnt != 5:
#     n = int(input())
#     if p[n] == 1:
#         continue
#     else:
#         p[n] = 1
#         cnt += 1
# print(*p)


# cities = input().split()
# while True:
#     for i in cities:
#         if len(i) > 5:
#             continue
#         else:
#             print('НЕТ')
#             break
#     print('ДА')
#     break


# students = input().split()
# i = 0
# check = 0
# while i < len(students):
#     if students[i][0].lower() == students[i][-1].lower():
#         check += 1
#     i += 1
# if check > 0:
#     print('ДА')
# else:
#     print('НЕТ')


# n = int(input())
# i = 1
# res = []
# if n < 100:
#     while i <= n:
#         if i % 3 == 0 and i % 5 == 0:
#             res.append(i)
#         i += 1
#     print(*res)
# else:
#     print('слишком большое значение n')


# n = int(input())
# i = 0
# while True:
#     if i ** 2 > n:
#         print(i)
#         break
#     i += 1


# print(sum([int(i) for i in input().split() if int(i) % 2 != 0]))

# print(*(len(i) for i in input().split()))


# n = int(input())
# print(*(i for i in range(1, n + 1) if n % i == 0), sep='\n')


# n = int(input())
# print(sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0))


# input_string = input()  # Ввод строки
# substring = "ра"
# indices = []
#
# index = input_string.find(substring)
# while index != -1:
#     indices.append(index)
#     index = input_string.find(substring, index + 1)
#
# if indices:
#     print(" ".join(map(str, indices)))
# else:
#     print(-1)


# text = input()
# index = text.find('ра')
# res = []
# while index != -1:
#     res.append(index)
#     index = text.find('ра', index + 1)
#
# if len(res) > 0:
#     print(*res)
# else:
#     print(-1)


# [a := input().lower(),
#  print(*([i - 1 for i in range(1, len(a)) if a[i] == 'а' and a[i - 1] == 'р'],
#          [-1])['ра' not in a])]


# text = "10+25 - 12"
# print(eval(text))


# nums = list(map(int, input().split()))
# print(*[i ** 2 for i in list(map(int, input().split()))])


# new_nums = []
# nums = list(map(float, input().split()))
# for i in nums:
#     if i < 0:
#         i = -1.0
#         new_nums.append(i)
#     else:
#         new_nums.append(i)
# print(*new_nums)

# nums = [i for i in list(map(float, input().split()))]
# print(*nums)


# print(*iter(input()))


# n = int(input())
# matrix = [[1 for _ in range(n)] for _ in range(n)]
#
# for row in matrix:
#     row[-1] = 5
#
# for row in matrix:
#     print(*row)


# print([abs(i) for i in list(map(float, input().split()))])

# n = int(input())
# matrix = [[1 if row == col else 0 for col in range(n)] for row in range(n)]
#
# for row in matrix:
#     print(*row)


# print(*[-1.0 if i < 0 else i for i in map(float, input().split())])


# n = int(input("Введите число n: "))
#
# prime_numbers = []
#
# for num in range(2, n):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_numbers.append(num)
#
# print(" ".join(map(str, prime_numbers)))


# n = int(input())
# print(*[i for i in range(1, n + 1) if n % i == 0])


# n = int(input())
# matrix = ([i] * n for i in range(n))
# for row in matrix:
#     print(*row)


# numbers = list(map(float, input().split()))
# for index, number in enumerate(numbers):
#     if index % 2 == 0:
#         print(number, end=' ')


# print(*[number for index, number in enumerate(list(map(float, input().split()))) if index % 2 == 0])


# print(*[sum(i) for i in zip(list(map(int, input().split())), list(map(int, input().split())))])

# n = input().split()
# data = []
# # print(*data)
#
# for i, p in enumerate(n):
#     # print(i, p)
#     if i % 2 == 0:
#         for j, k in enumerate(n):
#             if j % 2 == 1:
#                 data.append([p, int(k)])
#                 break
# print(data)


# cities = input().split()
# data = [[city, population] for city, population in
#         zip([j for i, j in enumerate(cities) if i % 2 == 0], [int(k) for l, k in enumerate(cities) if l % 2 != 0])]
# print(data)


# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# result = [lst_in[j][i] for j in range(len(lst_in) - 1,-1,-1) for i in range(len(lst_in[j]) - 1,-1,-1)]
# print(*result)

#
# numbers = list(map(int, input().split()))
#
# n = int(len(numbers) ** 0.5)  # Размерность матрицы
#
# lst = [[numbers[i * n + j] for j in range(n)] for i in range(n)]
#
# print(lst)


# print(*sorted(dict(pair.split('=') for pair in input().split()).items()))

# # симметричная матрица или нет
# matrix = []
# n = int(input())
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))
#
# flag = True
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             flag = False
# if flag:
#     print('Yes')
# else:
#     print('No')


# def list_sum_recursive(x):
#     if len(x) == 0:
#         return 0
#     if len(x) == 1:
#         return x[0]
#     return x[0] + list_sum_recursive(x[1:])


# def merge_two_list(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += a[i:]
#     if j < len(b):
#         c += b[j:]
#     return c
#
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     middle = len(s) // 2
#     left = merge_sort(s[:middle])
#     right = merge_sort(s[middle:])
#     return merge_two_list(left, right)
#
# print(mege_sort([]))


# n = int(input())
# summ = 0
# for i in range(n):
#     if (x := int(input())) > 0:
#         summ += x
# print(summ)


# n = int(input())
# summ = 0
# for i in range(n):
#     if (x := int(input())) > 0:
#         summ += x
# print(summ)


# n = int(input())
# for i in range(n):
#     if (x := int(input())) % 2 == 0:
#         print(x)

# n = int(input())
# minimum = float('inf')
# for i in range(n):
#     if (x := int(input())) < minimum:
#         minimum = x
# print(minimum)


# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x == 4 or x == 5:
#         continue
#     else:
#         print(x)


# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x < 0:
#         print('Тоши взломал тестирующую систему')
#     elif x < 60:
#         print('Сакура писала тест честно')
#     elif 60 <= x < 80:
#         print('Сакура списала с Мику')
#     elif 80 <= x <= 100:
#         print('Сакура списала с Тоши')
#     else:
#         print('Сакура взломала тестирующую систему')


# n = int(input())
# res = []
# for i in range(n):
#     res.append(int(input()))
# res.sort()
# if res[0] == res[1]:
#     print(min(res[0::]))
# else:
#     print(min(res[1::]))


# print(*[i for i in range(int(input()), int(input()), int(input()))], sep='\n')

# print(*[i for i in range(int(input()), int(input())) if i % 2 == 0], sep='\n')

# a, b = [int(input()) for i in range(2)]
# if a > b:
#     print(*[i for i in range(a, b, -1)], sep='\n')
# else:
#     print(*[i for i in range(a, b)], sep='\n')


# from math import factorial as f
# n = int(input())
# k = int(input())
# print(int(f(n) / (f(k) * f(n - k))))


# backpack = int(input())
# backpack_items = 0
# while backpack > 0:
#     x = int(input())
#     if x > backpack:
#         break
#     backpack -= x
#     backpack_items += 1
#
# print(backpack_items)


# count = 1
# while (x := input()) != 'Пентагон взломан':
#     count += 1
# print(count)


# n = int(input())
# count = 0
# while n != 1:
#     if n % 2 == 1:
#         n = (n * 3) + 1
#         count += 1
#     else:
#         n /= 2
#         count += 1
# print(count)

# print(text[:5] + '...' if len((text := input())) > 5 else text[:])

# text = input().split()
# res = []
# for i, v in enumerate(text):
#     if i % 2 == 0:
#         res.append(text[i] + ' ' + text[i + 1])
# print(*res, sep='\n')


# text = input()
# n = len(text) // 3
# print(text[:n])
# print(text[n:2 * n])
# print(text[2 * n:])


# print('YES' if (text := input()) == text[::-1] else 'NO')


# s = "Я не придумала тесты, так что представьте что они тут есть"
# print(s[::3])
# print(s[::-1])
# print(s[5:-5])
# print(s[4::2])


# print('YES' if (len((password := input())) >= 8 and password.lower() != password and password.upper() != password) else 'NO' )


# password = input()
# if len(password) >= 8 and password.lower() != password and password.upper() != password:
#     print('YES')
# else:
#     print('NO')


# s = "hello WORLD "
# print(s[len(s) // 2:] + s[:len(s) // 2])


# text = input().split()
# res = []
# for i, v in enumerate(text):
#     if i % 2 == 0:
#         res.append(v.title())
#     else:
#         res.append(v.lower())
# print(*res)


# text = input()
# n = int(len(text) / 2)
# print(text[:n].capitalize(), text[n:].lower(), sep='')


# message = input()
# print(message.find('Сакура'))


# print(input().count('@'))


# n = int(input())
# k = int(input())
# s = input().lower()
# count = 0
# for i in range(n):
#     text = input().lower()
#     if text in s:
#         count += 100
# print(count)


# print('YES' if input().isalnum() else 'NO')


# n = int(input())
# for i in range(n):
#     text = input()
#     if text.islower():
#         print(text)


# check = input()
# if check.isdigit():
#     print('Это число')
# elif check.isalpha():
#     print('Это слово')
# elif check.isalnum():
#     print('Это буквы и цифры')
# elif check.isspace():
#     print('Это строка из пробельных символов')
# else:
#     print('Это что-то странное')


# text = input()
# while 'Ё' in text or 'ё' in text:
#     text = text.replace('Ё', 'Е').replace('ё', 'е')
# print(text)


# print(input().replace('а', '').replace('А', ''))


# print(*['у' if i in 'аоуэыиеёяю' else i for i in input()], sep='')

# print(input().lower().strip() == input().lower())


# numbers = input().split()
# print(' + '.join(numbers), '=', sum([int(i) for i in numbers]))


# numbers = sorted(list(map(int, input().split())), reverse=True)
# n = int(input())
# for i in range(n):
#     a = int(input())
#     print(numbers[a - 1])


# n = int(input())
# matrix = []
# for row in range(n):
#     matrix.append([0] * n)
# for i in matrix:
#     print(*i)


# n = int(input())
# l = []
#
# for i in range(n):
#     row = []
#     for j in range(n):
#         if j < n / 2:
#             row.append(1)
#         else:
#             row.append(0)
#     l.append(row)
#
# for i in l:
#     for j in i:
#         print(j, end=" ")
#     print()


# n = int(input())
# m = int(input())
# res = []
# for i in range(n):
#     a = []
#     for j in range(1, m + 1):
#         a.append(j)
#     res.append(a)
# for i in res:
#     print(*i)


# n = int(input())
# l = []
#
# for i in range(n):
#     row = []
#     if i % 2 == 0:
#         for j in range(n):
#             if j % 2 == 0:
#                 row.append(0)
#             else:
#                 row.append(1)
#         l.append(row)
#     else:
#         for j in range(n):
#             if j % 2 == 0:
#                 row.append(1)
#             else:
#                 row.append(0)
#         l.append(row)
#
# for i in l:
#     print(*i)


# n = int(input())
# m = int(input())
# matrix = []
#
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(list(map(int, input().split())))
#     print(row)
#     break


# n, m = list(map(int, input().split()))
# print([[i for i in list(map(int, input().split()))] for j in range(n)])


# print([i for i in list(map(int, input().split())) if i % 2 == 0])


# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(abs(i - j), end=' ')
#     print()


# n, m = int(input()), int(input())
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         print(i * j, end='\t')
#     print()


# import random
#
#
# def card():
#     number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
#     suit = ['червей', 'бубно', 'треф', 'пик']
#     return str(random.choice(number)) + ' ' + str(random.choice(suit))
#
#
# print(card())


# morze_dict = {'А': '.-', 'Б': '-...', 'В': '.--',
#               'Г': '--.', 'Д': '-..', 'Е': '.',
#               'Ё': '.', 'Ж': '...-', 'З': '--..',
#               'И': '..', 'Й': '.---', 'К': '-.-',
#               'Л': '.-..', 'М': '--', 'Н': '-.',
#               'О': '---', 'П': '.--.', 'Р': '.-.',
#               'С': '...', 'Т': '-', 'У': '..-',
#               'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
#               'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
#               'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-',
#               'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
#               ' ': '-...-'}
# res = []
# text = input()
# for i in text.upper():
#     res.append(morze_dict.get(i))
# print(*res)


# morze = {".-": "А", "-...": "Б", ".--": "В", "--.": "Г", "-..": "Д", ".": "Е", "...-": "Ж", "--..": "З", "..": "И", ".---": "Й", "-.-": "К", ".-..": "Л", "--": "М", "-.": "Н", "---": "О", ".--.": "П", ".-.": "Р", "...": "С", "-": "Т", "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц", "---.": "Ч", "----": "Ш", "--.-": "Щ", ".--.-": "Ъ", "-.--": "Ы", "-..-": "Ь", "...-...": "Э", "..--": "Ю", ".-.-": "Я", "-...-": " "}
# res = []
# text = input().upper().split()
# for i in text:
#     if i == 'ё':
#         res.append('е')
#     else:
#         res.append(morze.get(i).lower())
# print(*res, sep='')


# print([round(i) for i in map(float, input().split(', '))])


# print(*[False if i == 0 else True for i in map(int, input().split())])


# start, stop = map(int, input().split(', '))
# res = []
# for i in range(stop, start - 1, -1):
#     res.append(i)
# print(*res, sep=', ', end=' ')


# nums = input().split(', ')
# print(*nums[0:-1:2], sep=', ')


# nums = input().split(', ')
# del nums[1:len(nums):2]
#
# print(*nums, sep=', ', end=' ')


# products = input().split()
# command = input().split()
# if command[0] == 'Добавить':
#     products.append(command[1])
#     print(*products)
# elif command[0] == 'Удалить':
#     if command[1] in products:
#         products.remove(command[1])
#         print(*products)
#     else:
#         print('Такого продукта нет в списке')


# nums = list(map(int, input().split()))
# minimum = min(nums)
# for i, v in enumerate(nums):
#     if v == minimum:
#         print(i)
#         break


# songs = input().split(', ')
# song = input().split(', ')
# songs.insert(int(song[1]), song[0])
# print(*songs, sep=', ')


# numbers = map(int, input().split())
# index = int(input())
# for i in numbers:
#     if i == index:
#         break
#     else:
#         print(i, end=' ')


# print(' '.join(input().lower().split()))


# print(*sorted(input().split()))


# start, stop = list(map(int, input().split()))
# while start <= stop:
#     print(start ** 3, end=' ')
#     start += 1


# n = int(input())
# i = 1
# while i <= n:
#     print('*' * i)
#     i += 1


# numbers = map(int, input().split())
# number = int(input())
#
# while True:
#     if number in numbers:
#         print('Есть')
#         break
#     else:
#         print('Нет')
#         break

# numbers = list(map(int, input().split()))
# n = int(input())
# i = 0
# while i < (len(numbers)):
#     if n not in numbers:
#         print('Числа нет!')
#         break
#     if numbers[i] == n:
#         print(i)
#         break
#     i += 1


# words = input().replace('', '').split(', ')
# res = []
# for i in words:
#     if i == '':
#         continue
#     res.append(i)
# print(*res, sep=', ')


# # -5 -8 -3 -9 -2 -7 -4 -6 -1 -10
# numbers = list(map(int, input().split()))
# max_number = float('-inf')
# index = 0
# while index < len(numbers):
#     if numbers[index] > max_number:
#         max_number = numbers[index]
#     index += 1
#
# print(max_number)


# n = int(input())
# summ = 0
# while n != 0:
#     summ += n % 10
#     n //= 10
# print(summ)


# summ = 0
# for i in range(24):
#     text = input().split(': ')
#     summ += float(text[1][:-2])
# print(round(summ / 24, 1))


# files = input().split()
# new_files = []
# for i in files:
#     if i.endswith('.jpg') or i.endswith('.jpeg'):
#         new_files.append(i)
# if new_files:
#     print(*sorted(new_files))
# else:
#     print('Картинок нет!')


# text = input().replace('.', '').replace(',', '').split()
# summ = 0
# for i in text:
#     if i.isdigit():
#         summ += int(i)
# print(summ)


# res = []
# text = input().split(', ')
# for i in text:
#     if i not in res:
#         res.append(i)
# print(*res, sep=', ')


# lesson = input().split(', ')
# for i, v in enumerate(lesson):
#     print(f'Урок {i + 1}: {v}')


# names = input().split(', ')
# index = list(map(int, input().split(', ')))
# for i, v in enumerate(names):
#     if i in index:
#         continue
#     print(v, end=' ')


# numbers = list(map(int, input().split(', ')))
# res = []
# for i, v in enumerate(numbers):
#     if v < 0:
#         res.append(i + 1)
# if res:
#     print(*res, sep=', ')
# else:
#     print('Убыточных месяцев не было')


# items = ['A', 'B', 'C']
# combinations = []
# for i in items:
#      for j in items:
#          combinations.append(i + j)
#
# print(combinations)
#
# ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=' ')
#     print()


# participants = input().split(', ')
# participants.sort()
#
# for i in range(len(participants)):
#     for j in range(i + 1, len(participants)):
#         print(participants[i], participants[j])


# numbers = list(map(int, input().split(', ')))
# n = int(input())
# combinations = []
#
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == n:
#             combinations.append((numbers[i], numbers[j]))
# if combinations:
#     for k in combinations:
#         print(*k, sep=', ')
# else:
#     print('Такую сумму получить нельзя!')


# n, m = map(int, input().split())
# field = [input().split() for _ in range(n)]
#
#
# def is_mine(cell):
#     return cell == '*'
#
#
# def is_closed(cell):
#     return cell == '?'
#
#
# def is_flag(cell):
#     return cell == 'x'
#
#
# def count_mines_around(x, y):
#     count = 0
#     for dx in [-1, 0, 1]:
#         for dy in [-1, 0, 1]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and is_mine(field[nx][ny]):
#                 count += 1
#     return count
#
#
# def game_result():
#     has_open_mine = False
#     has_closed_cell = False
#
#     for i in range(n):
#         for j in range(m):
#             cell = field[i][j]
#             if is_mine(cell) and cell != 'x':
#                 has_open_mine = True
#             elif is_closed(cell):
#                 has_closed_cell = True
#
#     if has_open_mine:
#         return "Проигрыш"
#     elif not has_closed_cell:
#         return "Выигрыш"
#     else:
#         return "Игра идёт"
#
#
# print(game_result())


# n = int(input())
# matrix = []
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f"{i*j: >2}", end=' ')
#     print()


# names = input().split(', ')
# points = list(map(int, input().split(', ')))
# print({name: points for name, points in zip(names, points)})


# students = input().split()
# grades = list(map(int, input().split()))
# dictt = {students: grades for students, grades in zip(students, grades)}
# for k, v in dictt.items():
#     if v >= 4:
#         print(k, end=' ')


# goals_1 = list(map(int, input().split(', ')))
# goals_2 = list(map(int, input().split(', ')))
# res = []
# for g1, g2 in zip(goals_1, goals_2):
#     if g1 > g2:
#         res.append('Победа')
#     elif g1 < g2:
#         res.append('Поражение')
#     else:
#         res.append('Ничья')
# print(*res, sep=', ')


# eagles = {
#     "John": 10,
#     "Michael": 15,
#     "David": 8,
#     "Daniel": 13,
#     "Andrew": 6
# }
#
# beavers = {
#     "Robert": 12,
#     "James": 7,
#     "William": 11,
#     "Thomas": 9,
#     "Matthew": 14
# }
#
# eagles.update(beavers)
# print(eagles)


# a, b, *c, d = input().split()
#
# print(a, d, *c, b)

#
# k, first = int(input()), {}
# for _ in range(k):
#     key, value = input().split(": ")
#     first.update({key: value})
#
# m, second = int(input()), {}
# for _ in range(m):
#     key, value = input().split(": ")
#     second.update({key: value})
#
# # Ваш код
# result = {**first, **second}
#
# print(result)


# print(*[i ** 2 for i in map(int, input().split(', '))], sep=', ')


# print({i: 0 for i in input().split(', ')})

# print(*[i[0] for i in input().split(', ')], sep=', ')

# print(*set([i for i in map(float, input().split()) if i > 0]))

# print(*[i for i in input().split() if i.isdigit()])

# fruits = [i for i in input().split()]
# letter = input()
# print(*(sorted(set([i for i in fruits if i[0] == letter]))))

# print(*[len(i) for i in input().split(', ') if i != ''], sep=', ')

# def maximums(*args):
#     return sorted(*args, reverse=True)[:2]
# numbers = map(int, input().split())
# largest1, largest2 = maximums(numbers)
# print(largest1, largest2)


# def calculate_statistics(values):
#     avg = sum(values) / len(values)
#     max_val = max(values)
#     min_val = min(values)
#     return avg, max_val, min_val
#
# data = list(map(float, input().split()))
# avg, max_val, min_val = calculate_statistics(data)
# print(avg, max_val, min_val)


# def in_interval(*args, **kwargs):
#     # print(*range(start, stop + 1))
#     # print(*[(range(start, stop + 1))])
#     return number in [int(i) for i in range(start, stop)]
#
# start, stop, number = map(int, input().split())
# print(in_interval(number))
# print(in_interval(start=start, stop=stop, number=number))


# lines = int(input())
# prefix = input()
# strings = [input() for _ in range(lines)]
#
# print(*list(map(lambda x: x.replace(prefix, ''), strings)))


# numbers = list(map(int, input().split()))
#
# print(*list(filter(lambda x: x % 5 == 0, numbers)))


# lines, athletes = int(input()), {}
#
# for _ in range(lines):
#     name, time = input().split(": ")
#     athletes.update({name: float(time)})
#
# fastest_runner = min(athletes, key=athletes.get)
#
# print(fastest_runner)


# values = input().split(", ")
# pairs = [(roman, int(arab)) for roman, arab in zip(values[::2], values[1::2])]
# print(max(pairs, key=lambda x: x[1])[0])


# class Athlete:
#     def __init__(self, name, results):
#         self.name = name
#         self.results = results
#
#     def average_time(self):
#         if len(self.results) == 0:
#             return 0.0  # Если список результатов пуст, вернем 0.0
#
#         total_time = sum(self.results)
#         average = total_time / len(self.results)
#         return round(average, 1)  # Округляем среднее время до одного знака после запятой
#
# # Считываем имя и результаты участника
# name = input()
# results = list(map(int, input().split()))
#
# # Создаем объект класса Athlete
# athlete = Athlete(name, results)
#
# # Вычисляем и выводим среднее время участника
# average_time = athlete.average_time()
# print(f"Среднее время участника {athlete.name}: {average_time} секунд")


# class Athlete:
#     def __init__(self, name, results):
#         self.name = name
#         self.results = results
#
#     def average_time(self):
#         return (sum([i for i in self.results]) / len(self.results))
#
#
#
# name = input()
# results = list(map(float, input().split()))
# participant = Athlete(name, results)
#
#         # Вычисление и вывод среднего времени
# average = participant.average_time()
# print(f"Среднее время участника {participant.name}: {average} секунд")


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0 and self.balance >= amount:
#             self.balance -= amount
#         else:
#             print('Недостаточно средств!')
#
#     def get_balance(self):
#         return self.balance
#
#
# # Создаем счет с начальным балансом
# initial_balance = int(input())
# account = BankAccount(initial_balance)
#
# # Пополняем счет
# account.deposit(int(input()))
#
# # Снимаем деньги
# account.withdraw(int(input()))
#
# # Получаем текущий баланс
# balance = account.get_balance()
# print(f"Текущий баланс: {balance}")


# N = int(input())
# a = [int(x) for x in input().split()]
# x = int(input())
#
# count = 0
#
# for i in a:
#     if i == x:
#         count += 1
# print(count)


# # Считываем данные в формате ключ=значение и разделяем их по пробелу
# input_data = input().split()
#
# # Инициализируем пустой словарь
# d = {}
#
# # Заполняем словарь данными из ввода
# for item in input_data:
#     key, value = item.split('=')
#     d[key] = value
#
# for k, v in d.items():
#     if k == 'False' or k == '3':
#         d.popitem(k)
#
# print(*sorted(d.items()))


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# d = {}
#
#
# # Заполняем словарь данными из ввода
# for item in lst_in:
#     number, name = item.split()
#     # print(parts)
#     if name not in d:
#         d[name] = [number]
#     else:
#         d[name].append(number)
#
# print(*sorted(d.items()))


# d = {}
# while (n := int(input())) != 0:
#     if n not in d:
#         d[n] = round(n ** 0.5, 2)
#         print(d.get(n))
#     else:
#         print(f'значение из кэша: {n}')


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# d = {}
#
# # здесь продолжайте программу (используйте список lst_in)
# for value in lst_in:
#     if value not in d:
#         d[value] = value
#         print(f'HTML-страница для адреса {d.get(value)}')
#     else:
#         print(f'Взято из кэша: HTML-страница для адреса {d.get(value)}')


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# d = {}
#
# # здесь продолжайте программу (используйте список lst_in)
#
# for item in lst_in:
#     day, name = item.split()
#     if day not in d:
#         d[day] = name
#     else:
#         d[day] += f', {name}'
#
# for day, name in d.items():
#     print(f'{day}: {name}')


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# # print(sorted(things.items(), key=lambda x: -x[1]))
# n = int(input()) * 1000
# backpack = 0
# res = []
# for key, value in sorted(things.items(), key=lambda x: x[1], reverse=True):
#     if backpack + value <= n:
#         backpack += value
#         res.append(key)
# print(*res)


# cities = input().split()
# if 'Ульяновск' in cities:
#     cities.remove('Ульяновск')
# print(*tuple(cities))


# print(*(i.lower() for i in input().lower().split() if 'ва' in i))

# numbers = map(int, input().split())
# res = []
# for i in numbers:
#     if i not in res:
#         res.append(i)
# print(*res)


# numbers = list(map(int, input().split()))
# res = []
# for index, value in enumerate(numbers):
#     if numbers.count(value) > 1:
#         res.append(index)
#
# print(*res)


# print(*sorted(map(float, input().split())))


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
#
# print(len(set([i.split(': ')[0] for i in lst_in])))


# res = set()
# while (city := input()) != 'q':
#     res.add(city)
# print(len(res))


# print(*sorted(set(input().split()) - set(input().split())))


# print(len({i for i in input().lower().split() if len(i) >= 3}))


# text = input().lower().split()
# res = {i: text.count(i) for i in text}
# print(res.get('и', 0))


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # Инициализация пустого словаря
# d = {}
#
# # Проходимся по каждой строке в списке
# for item in lst_in:
#     author, title = item.split(":")
#     author = author.strip()
#     title = title.strip()
#
#     # Если автор уже есть в словаре, добавляем название книги в его множество
#     if author in d:
#         d[author].add(title)
#     else:
#         # Если автора нет, создаем новую запись в словаре
#         d[author] = {title}


# def is_triangle(a, b, c):
#     return a + b > c


# def is_large(text):
#     return len(text) >= 3


# def is_odd(numbers):
#     res = []
#     for i in numbers:
#         if i % 2 != 0:
#             res.append(i)
#     return res
#
#
# numbers = list(map(int, input().split()))
# print(*is_odd(numbers))


# print(*[i for i in input().split() if len(i) >= 6])


# def f(x):
#     return x, len(x)
#
#
# cities = input().split()
# d = {city: len(city) for city in cities}
# print(*sorted(d, key=lambda x: d[x]))
#
#
# def multiply(maximum, minimum):
#     return maximum * minimum
#
#
# numbers = list(map(int, input().split()))
# maximum = max(numbers)
# minimum = min(numbers)
#
# print(multiply(maximum, minimum))
#
#
# # Алгоритм Евклида быстрый
# def get_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#     return a
#
#
# a, b = list(map(int, input().split()))
# print(get_nod(a, b))


# def get_rect_value(a, b, type=0):
#     if type == 0:
#         return (a * 2) + (b * 2)
#     else:
#         return a * b


# def check_password(password, chars='$%!?@#'):
#     flag = False
#     for i in chars:
#         if i in password:
#             flag = True
#             break
#
#     if len(password) >= 8 and flag:
#         return True
#     return False


# def convert(text, sep='-'):
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
#          'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
#          'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
#          'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     res = ''
#     for i in text:
#         if t.get(i) is None:
#             if i == ' ':
#                 res += sep
#             else:
#                 res += i
#         else:
#             res += t.get(i)
#     return res
#
# text = input().lower()
#
# print(convert(text, sep='-'))
# print(convert(text, sep='+'))


# def convert_to_tag(text, tag='div', up=True):
#     if up:
#         print(f'<{tag.upper()}>{text}</{tag.upper()}>')
#     print(f'<{tag}>{text}</{tag}>')
#
#
# text = input()
# convert_to_tag(text)


# def get_even(*args):
#     return [i for i in args if i % 2 == 0]


# def get_biggest_city(*args):
#     return max(args, key=len)


# def get_data_fig(*args, type=None, color=None, closed=None, width=None, **kwargs):
#     return (sum(args), [i: j for i, j in kwargs.items()])

# def get_data_fig(*args, **kwargs):
#     n = ['type', 'color', 'closed', 'width']
#     return (sum(args), *[kwargs[i] for i in n if i in kwargs])
#
#
# assert get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10) == (
# 45, False, 'Yellow', True, 10)
# assert get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10) == (
# 45, False, 'Yellow', True, 10)
# assert get_data_fig(5, 4, color='Yellow', type=False, closed=True) == (9, False, 'Yellow', True)
# print("OK")
#
# print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
# print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
# print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))


# *lst, x, y, z = list(map(int, input().split()))
# print(*lst)


# cities = input().split()
# lst_c = (*cities,)
# print(lst_c)


# a, b = map(int, input().split())
# print(*range(a, b + 1))


# numbers = list(map(float, input().split()))
# cities = input().split()
# print(*list(map(float, input().split())), *input().split())


# nums = list(map(int, input().split()))
# def get_rec_sum(nums)
#     return sum(nums)


# get_div = lambda x, y: x / y if y != 0 else None
# print(get_div(10, 0))


# def create_global(x):
#     global TOTAL
#     TOTAL = x


# def counter_add():
#     def counter(k):
#         return k + 5
#     return counter
#
#
# cnt = counter_add()
# k = int(input())
# print(cnt(k))


# def counter_add(n):
#     def counter(k):
#         return k + 5
#     return counter
#
#
#
# cnt = counter_add()
# k = int(input())
# print(cnt(k))


# def func_show(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Площадь прямоугольника: {result}")
#     return wrapper
#
#
# def get_sq(width, height):
#     return width * height


# def cyrillic_to_latin(s):
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#     s = s.lower()
#     for char in s:
#         if char in t:
#             s = s.replace(char, t[char])
#     return s
#
#
# def remove_chars(chars):
#     def decorator(func):
#         def wrapper(s):
#             for char in chars:
#                 s = s.replace(char, '-')
#             while '--' in s:
#                 s = s.replace('--', '-')
#             return s
#
#         return wrapper
#
#     return decorator
#
#
# s = input()
# chars = "?!:;,. "
#
#
# @cyrillic_to_latin
# @remove_chars(chars)
# def process_string(s):
#     return s
#
#
# result = process_string(s)
# print(result)


# try:
#     f = open("abc.txt")
#     try:
#         r = f.read(1)
#     finally:
#         f.close()
# except FileNotFoundError:
#     print('File Not Found')


# # ввод значений a и b (переменные a и b не менять!)
# a, b = map(int, input().split())
#
# # здесь продолжайте программу
#
# tp = (int(i ** 2) for i in range(a, b + 1))
# tp = tuple(tp)
# print(type(tp))


# def is_prost(x):
#     """ Функция нахождения простого числа"""
#     d = x - 1
#     if d < 0:
#         return False
#
#     while d > 1:
#         if x % d == 0:
#             return False
#         d -= 1
#     return True
#
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# b = filter(is_prost, a)
# lst = tuple(b)
# print(lst)


# lst = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск")
# b = filter(str.isalpha, lst)
# print(*b)


# cities = input().split()
# b = filter(lambda x: len(x) > 5, cities)
# for i in range(3):
#     print(next(b), end=' ')


# numbers = list(map(int, input().split()))
# res = filter(lambda x: len(str(abs(x))) == 2, numbers)
# print(*res)


# coins_1 = set(map(int, input().split()))
# coins_2 = set(map(int, input().split()))
# result = coins_1.intersection(coins_2)
# res = filter(lambda x: x % 2 == 0, result)
# print(*res)


# print(*[i + v for i, v in zip(sorted(map(int, input().split())), sorted(map(int, input().split()), reverse=True))])


# print(*sorted([i for i in input().split()], key=len, reverse=True))


# import sys
#
# # Считываем данные из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# Разбиваем первую строку на заголовки
# header = lst_in[0].split(';')

# # Инициализируем список для хранения данных
# data = []
#
# # Проходим по остальным строкам и разбиваем их на значения
# for line in lst_in[1:]:
#     values = line.split(';')
#     # Преобразуем числа в целые значения
#     values[0] = int(values[0])
#     values[2] = int(values[2])
#     data.append(values)
#
# # Сортируем данные по заданным критериям
# t_sorted = sorted(data, key=lambda x: (x[0], x[3], x[2], x[1]))
#
# # Выводим результат в формате "Имя;Зачет;Оценка;Номер"
# print(';'.join(header))
# for values in t_sorted:
#     print(';'.join(map(str, values)))


# def get_add(a, b):
#     if type(a) is not bool and type(b) is not bool:
#         if (isinstance(a, str) and isinstance(b, str)) or (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#             return a + b
#         else:
#             return None
#
#
# a = 3
# b = 4
# res = get_add(a, b)
# print(res)


# def get_sum(iter_object):
#     return sum([i for i in iter_object if isinstance(i, int) and type(i) != bool])
#
#
# print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))
# print(get_sum({5, 6, 7, '8', 5, '4'}))
# print(get_sum((10, "f", '33', True, 12)))
# print(get_sum(['1', True, False, (1, 23)]))


# def get_even_sum(it):
#     return sum([i for i in it if isinstance(i, int) and type(i) != bool and i % 2 == 0])


# def get_list_dig(lst):
#     return [i for i in lst if isinstance(i, (int, float))]


# ПРИМЕР СТЕКА
# x = [1, 2, 3]
# x.append(4)
# x.append(5)
# print(x)
#
# top = x.pop()
# print(top)
# print(x)
#
# top = x.pop()
# print(top)
# print(x)


# def closest_mod_5(x):
#     while x % 5 != 0:
#         x += 1


# def C(n, k):
#     if k == 0 or k == n:
#         return 1
#     else:
#         return C(n - 1, k) + C(n - 1, k - 1)
#
#
# n, k = map(int, input().split())
# print(C(n, k))


# class Counter:
#     def __init__(self, start=0):
#         self.count = start
#
#
# x1 = Counter(10)
# x = Counter()
# print(x.count)
# x.count += 1
# print(x.count)
# x.count += 1
# print(x.count)
# print(x1.count)


# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.coins = 0
#
#     def can_add(self, v):
#         return self.coins + v <= self.capacity
#
#     def add(self, v):
#         if self.can_add(v):
#             self.coins += v


# class Buffer:
#     def __init__(self):
#         self.sequence = []
#
#     def add(self, *a):
#         self.sequence += a
#         while len(self.sequence) >= 5:
#             print(sum(self.sequence[:5]))
#             self.sequence = self.sequence[5:]
#
#     def get_current_part(self):
#         return self.sequence


# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print("AssertionError")


# x = [-2, -1, 0, 1, 2]
# y = [i * i for i in x if i > 0]
# print(y)

# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#     def append(self, x):
#         if x <= 0:
#             raise NonPositiveError
#         super().append(x)


# banknotes = {
#     50: 0,
#     100: 0,
#     500: 0
# }
#
# while True:
#     banknote = input()
#     if banknote == "конец":
#         break
#     banknotes[int(banknote)] += 1
#
# for denomination, count in banknotes.items():
#     if count > 0:
#         print(f"{denomination} - {count}")
#     else:
#         print(f"{denomination} - 0")

# print(*(i for i in range(int(input()) + 1)), sep='\n')


# summ = 0
# for i in range(int(input()) + 1):
#     if i % 2 == 0:
#         summ += i
# print(summ)
#
#
# print(sum(i for i in range(int(input()) + 1) if i % 2 == 0))

# n = int(input())
# print(*(f'{i} * {n} = {i * n}' for i in range(1, 11, 1)), sep='\n')

# text = input()
# if '@' in text:
#     print('регистрация завершена')
# else:
#     print('вы указали неверную почту')
#
#
# print('регистрация завершена' if '@' in input() else 'вы неверно указали почту')

# base = list()
# for i in range(int(input())):
#     base.append(input())
# print(base)

# word_list = []
# while (word := input()) != 'сколько':
#     word_list.append(word)
# find_word = input()
# print(word_list.count(find_word))


# # не забудь указать параметры!!!
# # сколько их нужно указать?!
# def pas_gen(length, char):
#     password = ''
#     while len(password) != length:
#         password += (args)
#     print(res)
#
#
# pas_gen(12, ')


# def pas_gen(length=int(input()), char1=input(), char2=input(), char3=input(), char4=input()):
#     password = ""
#     chars = [char1, char2, char3, char4]
#     for i in range(length):
#         password += chars[i % 4]
#     print(password)



# def pas_gen(n: int, a: str, b: str, c: str, d: str) -> str:
#     password = ''
#     chars = [a, b, c, d]
#     while len(password) != n:
#         password += str([i for i in chars])
#
#     print(password)
#
#
# pas_gen(14, 'a', 'b', 'c', 'd')


# def pas_gen(num, char1, char2, char3, char4):
#     chars = [char1, char2, char3, char4]
#     password = ""
#     for i in range(num):
#         password += chars[i % 4]
#     print(password)
#
#
# def conversion(distance):
#     if distance > 0:
#         if len(str(distance // 10)) == 1:
#             return f'{distance // 10}.{distance % 10} см'
#         elif len(str(distance // 100)) == 1:
#             return f'{distance // 100}.{distance % 100 // 10 } дм'
#         elif len(str(distance // 1000)) == 1:
#             return f'{distance // 1000}.{distance % 1000 // 10 } м'
#         elif len(str(distance // 1000000)) == 1:
#             return f'{distance // 1000000}.{distance % 1000000 // 10 } км'
#
#
# def pas_gen(length, a, b, c, d):
#     print(''.join(([[a, b, c, d][i % 4] for i in range(length)])))
#
#
# dict = {'name':'Наталья', 'surname':'Морская пехота', 'age': 57}
# print({'name':'Наталья', 'surname':'Морская пехота', 'age': 57})


# # исходные данные
# tpl = (4.5, 756, 645.3, -34, 0, 12.3, -45.34, 77.01, 45)
# new_tpl = sorted(tpl[0::2])
# print(new_tpl[0] + new_tpl[-1])



# print(tuple(sorted(set(numbers := list(map(int, input().split()))), key=numbers.index)))


# lst = [(45, 13, 40), (4, 7, 37), (73, 80, 99), (10, 90, 33),
#        (1, 2, 3, 4), (567, 77, 20, 71), (1, 2, 3, 9)]
# print([(35,) + tpl[1:] for tpl in lst])


# tribonacci = [1, 1, 1]
# n = int(input())
#
# for i in range(3, n):
#     tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
#
# print(*tribonacci)


# # вводные данные
# lst = ['липкость', 'мыло', 'парк', 'цапля', 'утконос', 'папаня', 'лакомка'
#        'ель', 'титан', 'ласка', 'кратер', 'принтер', 'сало',
#        'поднос', 'ель', 'таракан', 'холодец', 'мрак', 'липкость',
#        'рык', 'парк', 'протез', 'пароль', 'школа', 'хрюкальник'
#        ]
#
# print(sum([1 for i in set(lst) if len(i) > 5]))


# print('ДА' if len(set(input().split() + input().split())) == 20 else 'НЕТ')


# print(*sorted(set(input().split()) ^ set(input().split()), key= lambda x: int(x)))


# # Вводные данные
# burger_1 = ['булочка', 'мясо', 'сыр', 'помидор', '"1000 островов"', 'красный лук']
# burger_2 = ['булочка', 'мясо', 'сыр', 'помидор', '"барбекю"', 'лук', 'огурец']
#
# # Выделяем базовые и дополнительные ингредиенты
# base_ingredients = sorted(set(burger_1) & set(burger_2))
# extra_ingredients = sorted((set(burger_1) | set(burger_2)) - set(base_ingredients))
#
# # Ввод суммы
# total_amount = int(input())
#
# # Распределяем сумму в соотношении 2:1
# base_amount = round(2/3 * total_amount, 1)
# extra_amount = round(1/3 * total_amount, 1)
#
# # Формируем итоговый словарь
# result = {
#     "Базовые ингредиенты": {
#         "Продукты": base_ingredients,
#         "Цена": base_amount
#     },
#     "Дополнительные ингредиенты": {
#         "Продукты": extra_ingredients,
#         "Цена": extra_amount
#     }
# }
#
# # Вывод результата в требуемом формате
# print(f"Базовые ингредиенты: {result['Базовые ингредиенты']}")
# print(f"Дополнительные ингредиенты: {result['Дополнительные ингредиенты']}")


# # вводные данные
# files = ['main.py', 'spisok.txt', '123.Py', 'paint.exe', 'tupik2003.mkv', 'foto.rar',
#          'tanecjivota.Mkv', 'RDR2.eXe', 'blacklist.Txt', 'lesson.py', 'foto2.rAr',                            'hack_pintagon.pY', 'lesson.py'
#          ]
#
# print(*sorted({i for i in files if i.lower().endswith('.py')}))


# numbers = [int('6' * i) for i in range(1, 667)]
# numbers = frozenset(numbers)
# print(*numbers)


# mask = "?46?44*2"
#
# d = '0123456789'
# dd = ['', *range(100)]
# ans = sorted([int(f'{x}46{y}44{z}2') for x in d for y in d for z in dd])
# for x in ans:
#     if x%6718==0:
#         print(x,x//6718)



# d = '0123456789'
# dd = ['', '00', *range(100)]
# ans1 = [int(f'4{x}5{y}6') for x in dd for y in dd]
# ans2 = [int(f'{x}74{z}68{y}') for x in d for y in d for z in dd]
# res = ans1 + ans2
# res.sort()
# itog = []
# for x in res:
#     if x % 2234 == 0:
#         itog.append([x, x // 2234])
#
#
# for i in sorted(itog):
#     print(*i)


# from fnmatch import fnmatch
#
# res = []
#
# for n in range(2234, 10 ** 11, 2234):
#     if fnmatch(str(n), '4*5*6'):
#         if n % 2234 == 0:
#             res.append([n, n // 2234])
# for n in range(2234, 10 ** 11, 2234):
#     if fnmatch(str(n), '?74*68?') and n % 2234 == 0:
#         if n % 2234 == 0:
#             res.append([n, n // 2234])
# res.sort()
# for i in res:
#     print(*i)

#
# from fnmatch import fnmatch
#
# ans1 = [[num, num // 2234] for num in range(2234, 10 ** 10 + 1,  2234) if (fnmatch(str(num), '4*5*6') == True) and (num % 2234 == 0)]
# ans2 = [[num, num // 2234] for num in range(2234, 10 ** 10 + 1, 2234) if (fnmatch(str(num), '?74*68?') == True) and (num % 2234 == 0)]
# res = []
# res.extend(ans1)
# res.extend(ans2)
#
# for i in sorted(res):
#     print(*i)

# n = int(input())
# for i in range(1, n + 1):
#     string = input()
#     if len(string.split()) == 0:
#         print(f'{i}: COMMENT SHOULD BE DELETED')
#     else:
#         print(f'{i}: {string}')


# number = input().split('_')
# base = 'АВЕКМНОРСТУХ'

# if (len(number[-1]) == 2 or len(number[-1]) == 3) and number[-1].isdigit() and len(number[0]) == 6:
#     if (number[0][0] in base) and (number[0][4] in base) and number[0][5] in base:
#         print('1 cycle success')
#         if number[0][0].isalpha():
#             print('2 cycle success')
#             if (number[0][1:4]).isdigit():
#                 print('3 cycle success')
#                 if number[0][4].isalpha():
#                     if number[0][5].isalpha():
#                         print('YES')
#     else:
#         print('NO')


# if (len(number[-1]) == 2 or len(number[-1]) == 3) and number[-1].isdigit() and len(number[0]) == 6:
#     if (number[0][0] in base) and (number[0][4] in base) and (number[0][5] in base):
#         if number[0][0].isalpha() and (number[0][1:4]).isdigit() and number[0][4].isalpha() and number[0][5].isalpha():
#             print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')


# p = '@rrrrrrrabban666'
#
# print((p.isalnum()))
# print((p.islower()))
#
#
# nickname = input()
#
# if nickname.startswith('@') and (5 <= len(nickname) <= 15) and nickname[1:].isalnum():
#     if nickname[1:].isdigit():
#         print('Correct')
#     else:
#         if nickname[1:].islower():
#             print('Correct')
#         else:
#             print('Incorrect')
# else:
#     print('Incorrect')


# print(chr(ord('🐍')))
# print(ord('1'))
# print(ord(chr(128013)))
# print(chr(128013))


# res = []
#
# for _ in range(4):
#     word = input()
#     max_sum = sum([ord(i) for i in word])
#     res.append([max_sum, word])
#
# print(max(res, key=lambda x: x[0])[-1])




# message = input()
# eng_to_rus = str.maketrans("eyopaxcETOPAHXCBM", "еуорахсЕТОРАНХСВМ")
# old_cost = sum([ord(i) * 3 for i in message])
# new_message = message.translate(eng_to_rus)
# new_cost = sum([ord(i) * 3 for i in new_message])
#
# print(f"Старая стоимость: {old_cost}🐝")
# print(f"Новая стоимость: {new_cost}🐝")
#


# import re
#
# # Input: text with encoded Russian letters
# text = input()
#
# # Function to decode [u-<unicode>] to corresponding character
# def decode_russian_letters(match):
#     unicode_value = int(match.group(1))
#     return chr(unicode_value)
#
# # Regex pattern to find encoded letters
# pattern = r"\[u-(\d+)\]"
#
# # Replace all occurrences of the pattern with decoded characters
# decoded_text = re.sub(pattern, decode_russian_letters, text)
#
# # Output the decoded text
# print(decoded_text)



# letter = 'АБВГДЕЖЗИЙКЛМНОП'
# res = []
# for _ in range(int(input())):
#     school_class = input()
#     if len(school_class) == 2:
#         if school_class[0].isdigit() and (school_class[1] in letter):
#             res.append('YES')
#         else:
#             res.append('NO')
#     else:
#         res.append('NO')
# print(*res, sep='\n')



# res = [input() for _ in range(3)]
# minimum = min(res)
# maximum = max(res)
# middle = [i for i in res if i != min(res) and i != max(res)]
# print(minimum, *middle, maximum)




# books = [input().strip() for _ in range(int(input()))]
# res = []
# for book in books:
#     author_title = book.split(", ")
#     surname = author_title[0].split()[0]
#     title = author_title[1]
#     res.append((surname, title))
#
# if res == sorted(res):
#     print("YES")
# else:
#     print("NO")


# secret_word = input()
# count = [secret_word.count(i) for i in secret_word]
# dictt = {}
# word = ''
#
# for _ in range(int(input())):
#     phrase = input().split(': ')
#     dictt.update({(int(phrase[-1])):(phrase[0])})
#
# for i in count:
#     word += dictt.get(i)
#
# print(word)



# import random
#
# ascii = '23456789abcdefghigkmnpqrstuvyxwzABCDEFGHGKLMNPQRSTUVYXWZ'
#
#
# def generate_password(length):
#     password = ''
#     while len(password) < length:
#         password += random.choice(ascii)
#     return password
#
# def generate_passwords(count, length):
#     return '\n'.join([generate_password(length) for _ in range(count)])
#
# n, m = int(input()), int(input())
#
#
# print(generate_passwords(n, m))


# import random
# import string
#
# nums = '23456789'
# lower_case = 'abcdefghigkmnpqrstuvyxwz'
# upper_case = 'ABCDEFGHJKLMNPQRSTUVYXWZ'
# allchars = list(set(string.ascii_letters + string.digits) - set("lI1oO0"))
#
# def generate_password(length):
#     while True:
#         password = [
#             random.choice(lower_case),
#             random.choice(upper_case),
#             random.choice(nums),
#         ]
#         password += random.choices(allchars, k=length - 3)
#
#         random.shuffle(password)
#         if (
#             any(c.islower() for c in password)
#             and any(c.isupper() for c in password)
#             and any(c.isdigit() for c in password)
#         ):
#             return ''.join(password)
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
#
# n = int(input())
# m = int(input())
#
# for pwd in generate_passwords(n, m):
#     print(pwd)


# users = [('Timur', 28), ('Ruslan', 21), ('Roman', 30), ('Soltan', 24), ('Robert', 1)]
# result = max(users, key=lambda x: x[1])
# print(result)



# from functools import reduce
#
# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = filter(lambda x: x % 2 == 1, obj)
# result = reduce(lambda x, y: x + y, obj, 0)
#
# print(result)



# from itertools import combinations
#
# # Ввод строки и преобразование в список
# input_list = input().split()
#
# # Список для хранения всех подсписков
# sublists = [[]]
#
# # Генерация подсписков
# for length in range(1, len(input_list) + 1):
#     for combination in combinations(input_list, length):
#         sublists.append(list(combination))
#
# # Вывод результата
# print(sublists)



# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)



# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# primary = sorted(list(filter(lambda x : x[1] > 10000000 and x[2] == 'primary', data)))
# cities = [i[0] for i in primary]
# print('Cities:', ', '.join(cities))



# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
#
# def func_apply(func, lst):
#     return [func(i) for i in lst]
#
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))



# func = lambda x: x[0].lower() == 'a' and x[-1].lower() == 'a'
#
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))



# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for country, city, pop_amount in zip(countries, capitals, population):
#     print(f'{city} is the capital of {country}, population equal {pop_amount} people.')



# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(list(map(lambda word: word in command, ignore)))
#
#
# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))



# abscissas, ordinates, applicates = ([i for i in map(float, input().split())] for _ in range(3))
# print(all((x ** 2) + (y ** 2) + (z ** 2) <= 2 ** 2 for x, y, z in zip(abscissas, ordinates, applicates)))



# ip_address = input().split('.')
# print(all(list(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, ip_address))))



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