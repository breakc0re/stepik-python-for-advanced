# Задача: Камень, ножницы, бумага

timur = input()
ruslan = input()

if timur == 'камень' and ruslan == 'ножницы':
    print('Тимур')
elif timur == 'ножницы' and ruslan == 'бумага':
    print('Тимур')
elif timur == 'бумага' and ruslan == 'камень':
    print('Тимур')
elif timur == ruslan:
    print('ничья')
else:
    print('Руслан')
