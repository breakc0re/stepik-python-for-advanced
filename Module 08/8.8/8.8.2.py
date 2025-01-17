# Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее первую букву
# каждого слова (в нижнем регистре) списка words. Результат вывести на одной строке в алфавитном порядке,
# разделяя элементы одним символом пробела.


words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
         'tangerine', 'Watermelon', 'currant', 'Almond']

new_words = {i.lower()[0] for i in words}

print(*sorted(new_words))
