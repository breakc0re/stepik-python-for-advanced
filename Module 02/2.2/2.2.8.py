# Задача: Камень, ножницы, бумага, ящерица, Спок 🌶️


def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Ничья"
    elif (choice1 == "камень" and choice2 in ["ножницы", "ящерица"]) or \
            (choice1 == "ножницы" and choice2 in ["бумага", "ящерица"]) or \
            (choice1 == "бумага" and choice2 in ["камень", "Спок"]) or \
            (choice1 == "ящерица" and choice2 in ["бумага", "Спок"]) or \
            (choice1 == "Спок" and choice2 in ["камень", "ножницы"]):
        return "Тимур"
    else:
        return "Руслан"


# Считываем выбор Тимура и Руслана
choice1 = input()
choice2 = input()

# Определяем победителя
winner = determine_winner(choice1, choice2)

# Выводим результат
print(winner)
