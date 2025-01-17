# Максимальный в области 1


# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.


n = int(input())
matrix = []
maximum = float('-inf')

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    for j in range(i + 1):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
