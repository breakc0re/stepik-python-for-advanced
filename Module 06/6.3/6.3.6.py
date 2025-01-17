# Конкурсный отбор


# Решение №1

n = int(input())
students_list = []
new_students_list = []

for _ in range(n):
    text = input().split()
    students_list.append(text)

for i in students_list:
    if int(i[1]) >= 4:
        new_students_list.append(i)

for j in students_list:
    print(*j, end='\n')

print()

for k in new_students_list:
    print(*k, end='\n')


# Решение №2 (более короткое)

n = int(input())
students_list = [input().split() for _ in range(n)]

for student in students_list:
    print(*student)

print()

for name, grade in students_list:
    if int(grade) >= 4:
        print(name, grade)
