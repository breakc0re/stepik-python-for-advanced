# Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа
# от 1 до 15 (включительно), а значения представляют собой квадраты ключей.

# Примечание. Выводить содержимое словаря result не нужно.


result = {num: num ** 2 for num in range(1, 16)}
