# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
#
# matrix = [[2, 3, 1, 0],
#           [9, 4, 6, 8],
#           [4, 7, 2, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()
#



# n = 50
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
# print(matrix)
#
# for i in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
#
# for r in range(n):                     # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()


# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])
# print((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)[:7])
#
# print(('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')[2:])
# print(('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')[:-3])
# print(('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')[3:-2])
# print(len(('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')))


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# new_numbers = []
# for i in numbers:
#     new_numbers.append(sum(list(i))/len(i))
# print(new_numbers)
