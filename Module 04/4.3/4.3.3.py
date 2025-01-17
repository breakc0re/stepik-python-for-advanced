# Треугольник Паскаля 1 🌶️


def pascal(n):
    if n == 0:
        return [1]
    else:
        pre_row = pascal(n - 1)
        row = [1]
        for i in range(len(pre_row) - 1):
            row.append(pre_row[i] + pre_row[i + 1])
        row.append(1)
        return row


n = int(input())
triangle_row = pascal(n)
print(triangle_row)
