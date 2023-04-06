"""
Даны два массива чисел. Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""
import random

# import random
#
# n = int(input('Введите число N (длина списка 1): '))
# m = int(input('Введите число M (длина списка 2): '))
#
# list_1 = [random.randint(1, 20) for i in range(n)]
# list_2 = [random.randint(1, 20) for i in range(m)]
#
# print(list_1)
# print(list_2)
#
# list_3 = list()
#
# for item in list_1:
#     if list_2.count(item) == 0:
#         list_3.append(item)
#
# print(list_3)

"""
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного
"""

# list_1 = [random.randint(1, 10) for _ in range(10)]
#
# count = 0
#
# for i in range(len(list_1)):
#     if list_1[i - 2] < list_1[i - 1] and list_1[i] < list_1[i - 1]:
#         count += 1
#
# print(list_1)
# print(count)

"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

# list_1 = [random.randint(1, 10) for _ in range(10)]
# print(list_1)
#
# count = 0
#
# for item in list_1:
#     for i in range(len(list_1)):
#
#     print(list_1.count(item) % 2)
#     if list_1.count(item) % 2 == 0:
#         count += 1
#
# print()
# print(count)


"""

"""
