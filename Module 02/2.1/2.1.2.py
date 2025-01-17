# Задача: Индекс массы тела

weight = float(input())
height = float(input())

bmi = weight / (height * height)

if 25 >= bmi >= 18.5:
    print('Оптимальная масса тела')
elif bmi < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')
