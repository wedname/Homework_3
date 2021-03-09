"""
Задание 1
Напишите программу, которая запрашивает два
целых числа x и y, после чего вычисляет и выводит
значение x в степени y.
"""

number = None
power = None
result = 1

while True:
    number = input("Введите число: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print("Не число!")
        continue

while True:
    power = input("Введите степень: ")
    if power.isdigit():
        break
    else:
        print("Не число!")
        continue

for i in range(1, int(power)+1):
    result *= number
print(result)

"""
Задание 2
Подсчитать количество целых чисел в диапазоне от
100 до 999 у которых есть две одинаковые цифры.
"""

count_same = 0
for i in range(100, 1000):
    i1 = i // 100  # Первая цифра
    i2 = i // 10 % 10  # Вторая цифра
    i3 = i % 10  # Третья цифра
    if i1 == i2 or i2 == i3 or i1 == i3:
        # print(i)
        count_same += 1
print(count_same)

"""
Задание 3
Подсчитать количество целых чисел в диапазоне от
100 до 9999 у которых все цифры разные.
"""

count_various = 0
for i in range(100, 1000):
    i1 = i // 100  # Первая цифра
    i2 = i // 10 % 10  # Вторая цифра
    i3 = i % 10  # Третья цифра
    if i1 != i2 and i2 != i3 and i1 != i3:
        # print(i)
        count_various += 1

for i in range(1000, 10000):
    first = i // 100
    i1 = i // 1000
    i2 = i // 100 % 10

    second = i % 100
    i3 = i // 10 % 10
    i4 = i % 10
    if i1 != i2 and i2 != i3 and i3 != i4 and i1 != i3 and i1 != i4 and i2 != i4:
        count_various += 1
print(count_various)

"""
Задание 4
Пользователь вводит любое целое число. Необхо-
димо из этого целого числа удалить все цифры 3 и 6 и
вывести обратно на экран.
"""

number = None

while True:
    number = input(f"Введите целое число: ")
    if number.isdigit():
        break
    else:
        print("Не целое число!")
        continue

for char in number:
    number = number.replace('3', '')
    number = number.replace('6', '')
print(number)


