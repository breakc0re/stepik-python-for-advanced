# Упаковка дубликатов 🌶️


text = input().split()

result = []
current = []
pre_sym = None

for sym in text:
    if sym == pre_sym:
        current.append(sym)
    else:
        if current:
            result.append(current)
        current = [sym]
        pre_sym = sym

if current:
    result.append(current)

print(result)
