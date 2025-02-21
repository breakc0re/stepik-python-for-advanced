# Количество слов в тексте


# Напишите программу для определения общего количества различных слов в строке текста.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.

# Примечание 1. Словом считается последовательность не пробельных символов, идущих подряд,
# слова разделены одним или большим числом пробелов.

# Примечание 2. Знаками препинания .,;:-?! пренебрегаем.


# Решение № 1

unique_words = set()
text = input().lower().split(' ')

for word in text:
    unique_words.add(word.strip('.,;:-?!'))

print(len(unique_words))

# Решение № 2 (короткое)

# words = [word.lower().strip('.,;:-?!') for word in input().split()]

# print(len(set(words)))
