# Задача: Роскомнадзор запретил букву а 🌶️🌶️

word = input() + ' запретил букву'
alphabet = 'абвгдежзийклмнопрстуфхцчшщьъэюя'
for sym in alphabet:
    if sym in word:
        print(word, sym)
        word = word.replace(sym, '').replace('  ', ' ').strip()
