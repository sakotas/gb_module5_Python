"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
import random

# n, m = input("Введите кол-во элементов n и m через пробел: ").split(' ')
#
# print(n, m)
#
# n_list = list()
# m_list = list()
#
# for i in range(int(n)):
#     n_list.append(int(input(f'Введите число в массиве "n" на место {i+1} из {n} в списке: ')))
#
# for i in range(int(m)):
#     m_list.append(int(input(f'Введите число в массиве "m" на место {i+1} из {m} в списке: ')))
#
# print(n_list)
# print(m_list)
#
# join_list = n_list + m_list
# join_list.sort()
#
# print(set(join_list))

"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""

chernika_list = [random.randint(1, 5) for _ in range(5)]
# chernika_list = [3, 3, 1, 4, 5]

print(chernika_list)

max_value = 0

for i in range(len(chernika_list)):
    if i == 0:
        max_value = chernika_list[i] + chernika_list[i + 1] + chernika_list[len(chernika_list) - 1]
    elif i == len(chernika_list)-1:
        if max_value < chernika_list[i] + chernika_list[0] + chernika_list[i-1]:
            max_value = chernika_list[i] + chernika_list[0] + chernika_list[i-1]
    elif max_value < chernika_list[i-1] + chernika_list[i] + chernika_list[i+1]:
        max_value = chernika_list[i-1] + chernika_list[i] + chernika_list[i+1]

print(max_value)
