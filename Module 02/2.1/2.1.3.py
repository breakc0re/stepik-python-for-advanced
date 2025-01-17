# Задача: Стоимость строки

text = input()

rub = (len(text) * 60) // 100
kop = (len(text) * 60) % 100

print(f'{rub} р. {kop} коп.')
