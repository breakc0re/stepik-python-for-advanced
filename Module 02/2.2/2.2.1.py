# Задача: Координатные четверти

point = int(input())
first, second, third, fourth = 0, 0, 0, 0

for i in range(point):
    x, y = map(int, input().split())
    print(x > 0 and y > 0)
    first += x > 0 and y > 0
    second += x < 0 < y
    third += x < 0 and y < 0
    fourth += x > 0 > y

print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")
