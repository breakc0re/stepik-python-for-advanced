# Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом
# (в зависимости от переданных аргументов) она должна вести себя так:

# matrix() — возвращает матрицу 1 × 1, в которой единственное число равно нулю.
# matrix(n) — возвращает матрицу n × n, заполненную нулями.
# matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями.
# matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый элемент равен числу value.

# При создании функции пользуйтесь аргументами по умолчанию.

# Примечание 1.
# Приведенный ниже код:

# print(matrix())  # матрица 1 × 1 из 0
# print(matrix(3))  # матрица 3 × 3 из 0
# print(matrix(2, 5))  # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9

# должен выводить:

# [[0]]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]

# Примечание 2.
# Вызывать функцию matrix() не нужно, требуется только реализовать ее.


# Решение №1
def matrix(n=None, m=None, value=None):
    if n is None and m is None and value is None:
        return [[0]]
    elif n is not None and m is None and value is None:
        return [[0] * n for _ in range(n)]
    elif n is not None and m is not None and value is None:
        return [[0] * m for _ in range(n)]
    return [[value] * m for _ in range(n)]


print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))


# Решение №2
# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     return [[value] * m for _ in range(n)]
