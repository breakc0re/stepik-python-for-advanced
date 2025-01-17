# Задача: Орел и решка


max_count = 0
current_count = 0

text = input().lower()

for i in text:
    if i == 'р':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)


# хитрое короткое решение с методом split()

# s = input().split('О')
# print(len(max(s)))