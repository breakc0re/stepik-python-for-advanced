# Одинаковые цифры


# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

# Формат входных данных
# На вход программе подаются два натуральных числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.


print('NO' if set(input()).isdisjoint(set(input())) else 'YES')
