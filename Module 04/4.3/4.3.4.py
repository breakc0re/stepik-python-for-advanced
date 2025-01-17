# Треугольник Паскаля 2


n = int(input())
triangle = []

for i in range(n):
    if n == 0:
        triangle = [1]
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
for k in triangle:
    print(*k)
