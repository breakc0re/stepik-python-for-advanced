# Задача: Задача Иосифа Флавия 🌶️🌶️

def josephus(n, k):
    # Создаем список с номерами людей от 1 до n
    circle = list(range(1, n + 1))
    index = 0

    while len(circle) > 1:
        # Вычисляем индекс человека, который выбывает из круга
        index = (index + k - 1) % len(circle)
        # Удаляем выбывшего человека из списка
        circle.pop(index)

    return circle[0]  # Возвращаем номер последнего оставшегося человека


# Считываем входные данные
n = int(input())
k = int(input())

# Вызываем функцию и выводим результат
result = josephus(n, k)
print(result)
