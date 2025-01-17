# Задача: Сдвиг в развитии

numbers = [int(n) for n in input().split()]
numbers.insert(0, numbers[-1])
del numbers[-1]

print(*numbers)


# Второе решение со срезами, более лаконичное.

# a = input().split()
# print(*[a[-1]] + a[:-1])
