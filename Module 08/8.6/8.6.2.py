# Общие числа


# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит
# все числа в порядке возрастания, которые есть как в первой строке, так и во второй.

# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести множество чисел, встречающихся в обеих строках.


print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))
