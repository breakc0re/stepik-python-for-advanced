# Неповторимые цифры


# На вход программе подается строка, состоящая из цифр. Необходимо определить,
# верно ли, что в ее записи ни одна из цифр не повторяется?

# Формат входных данных
# На вход программе подается строка, состоящая из цифр

# Формат выходных данных
# Программа должна вывести YES если ни одна из цифр в строке не повторяется и NO в противном случае.


print('YES' if len(set((n := input()))) == len(n) else 'NO')
