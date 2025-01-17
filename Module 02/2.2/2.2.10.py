# Задача: Кремниевая долина 🌶️🌶️


number = int(input())
final_res = []

for i in range(1, number + 1):
    text = input()
    res = ''
    for symbol in 'anton':
        if symbol in text:
            res += symbol
            text = text[text.find(symbol):]
    if res == 'anton':
        final_res.append(i)
print(*final_res)
