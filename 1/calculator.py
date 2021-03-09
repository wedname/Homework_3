"""
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/
"""

number_1 = None
number_2 = None
operation = ['+', '-', '*', '/']

while True:
    while True:
        try:
            number_1 = float(input("Введите первое число: "))
        except ValueError:
            print("Не число!")
            continue
        else:
            break

    while True:
        user_operation = input("Введите операцию (+, -, *, /), если хотите закрыть программу - нажмите 0: ")
        if user_operation in operation:
            break
        elif user_operation == '0':
            exit()
        else:
            print("Такой операции нет!")
            continue

    while True:
        try:
            number_2 = float(input("Введите второе число: "))
        except ValueError:
            print("Не число!")
            continue
        else:
            break

    if user_operation == '+':
        result = number_1 + number_2
        print(result)
    elif user_operation == '-':
        result = number_1 - number_2
        print(result)
    elif user_operation == '*':
        result = number_1 * number_2
        print(result)
    elif user_operation == '/':
        result = number_1 / number_2
        print(result)
