"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
import random

first_elem = int(input('Введите 1-й элемент: '))
div = int(input('Введите разность: '))
quantity = int(input('Введите кол-во элементов: '))

new_list = list()
new_list.append(first_elem)

for elem in range(quantity-1):
    first_elem = first_elem + div
    new_list.append(first_elem)
    print(first_elem)

print(new_list)

"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

new_list = [random.randint(0, 100) for _ in range(10)]

print(new_list)

min_value = int(input('Введите min: '))
max_value = int(input('Введите max: '))

index_list = list()

for elem in range(len(new_list)):
    if min_value < new_list[elem] < max_value:
        index_list.append(elem)

print(index_list)
