# Анаграммы 1


# Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово
# (или словосочетание). Например, английские слова evil и live – это анаграммы.

# На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

# Формат входных данных
# На вход программе подаются два слова, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести YES если слова являются анаграммами и NO в противном случае.


print('YES' if sorted(input()) == sorted(input()) else 'NO')
