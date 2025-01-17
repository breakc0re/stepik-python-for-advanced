# Три слова


# На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех
# трех слов был использован один и тот же набор букв?

# Формат входных данных
# На вход программе подается строка, состоящая из трех слов.

# Формат выходных данных
# Программа должна вывести YES, если для записи всех трех слов был использован
# один и тот же набор букв и NO в противном случае.


text = input().split()

print('YES' if set(text[0]) == set(text[1]) == set(text[2]) else 'NO')
