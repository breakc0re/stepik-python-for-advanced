# Книги на прочтение 🌶️


# Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

# "Что такое математика?";
# "Математическая составляющая";
# "100 гениальных идей по математике".

# Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью.
# Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе,
# z учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников.
# Всего в 10 классе учится a учеников. Напишите программу, которая выводит сколько учеников:

# прочитали только одну книгу;
# прочитали две книги;
# не прочитали ни одной из рекомендованных книг.

# Формат входных данных
# На вход программе подаются числа n,m,k,x,y,z,t,a, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.


n, m, k, x, y, z, t, a = [int(input()) for i in range(8)]
s1 = n + m - x - t
s2 = m + k - y - t
s3 = k + n - z - t
s = (n - s1 - s3 - t) + (m - s1 - s2 - t) + (k - s2 - s3 - t)
print(s)
print(s1 + s2 + s3)
print(a - s - s1 - s2 - s3 - t)
