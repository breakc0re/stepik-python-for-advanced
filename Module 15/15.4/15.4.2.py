# Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от
# начала координат (точки (0;0)). Программа должна вывести отсортированный список.

# Примечание. Расстояние от начала координат O(0;0) до точки A(x;y) равно OA = sqrt(x ** 2 + y ** 2)

# Примечание. Используйте необязательный аргумент key.

from math import sqrt

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def formula(item):
    return sqrt(item[0] ** 2 + item[1] ** 2)


print(sorted(points, key=formula))
