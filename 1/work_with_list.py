"""
В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчи-
тать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.
"""


list_of_numbers = [65, 98, -13, 9, 0, -5, 0, -1, 102]
min_value = list_of_numbers[0]
max_value = list_of_numbers[0]
count_negative = 0
count_positive = 0
count_zero = 0

print(list_of_numbers)

for i_min in list_of_numbers:
    if i_min < min_value:
        min_value = i_min
print(f"Минимальное значение списка: {min_value}")

for i_max in list_of_numbers:
    if i_max > max_value:
        max_value = i_max
print(f"Максимальное значение списка: {max_value}")

for c in list_of_numbers:
    if c < 0:
        count_negative += 1
print(f"Кол-во отрицательных чисел: {count_negative}")

for c in list_of_numbers:
    if c > 0:
        count_positive += 1
print(f"Кол-во положительных чисел: {count_positive}")

for c in list_of_numbers:
    if c == 0:
        count_zero += 1
print(f"Кол-во нулей: {count_zero}")
