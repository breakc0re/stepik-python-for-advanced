# Секретное слово


# Напишите программу для расшифровки секретного слова методом частотного анализа.

# Формат входных данных
# В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
# В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

# Формат выходных данных
# Программа должна вывести дешифрованное слово.

# Примечание. Гарантируется, что частоты букв не повторяются.


encrypted_word = input()
n = int(input())
frequency_dict = {}
for _ in range(n):
    letter, frequency = input().split(': ')
    frequency_dict[letter] = int(frequency)

decrypted_word = ''
for letter in encrypted_word:
    if letter.isalpha():
        decrypted_word += max(frequency_dict, key=frequency_dict.get)
    else:
        decrypted_word += letter

print(decrypted_word)

