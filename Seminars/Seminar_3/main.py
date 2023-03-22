import random as rnd

# mylist = []
#
# for i in range(10):
#     if i % 2 == 0:
#         mylist.append(i)
#         print(i)
#
# print(mylist)
#
# new_list = [i for i in range(10) if i % 2 == 0]
# print(new_list)
#
#
# def func(x, y):
#     return x * y
#
#
# print(func(4, 5))
# print((lambda x, y: x * y)(4, 5))

# numb_list = [rnd.randint(0, 20) for _ in range(40)]

# my_tuple = (1, 2, 3, 4)
# a, b, c, d = my_tuple

# print(numb_list)
# numb_set = set(numb_list)
#
# print(len(numb_set)) # todo finish function


"""
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
K – положительное число.
"""

# task1_list = [rnd.randint(0, 20) for _ in range(10)]
# print(f"Создан список: {task1_list}")
# k = int(input("Введите число К: "))
#
# for i in range(k):
#     task1_list.insert(0, task1_list.pop())
#
# print(task1_list)

"""
Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, 
больших предыдущего (элемента с предыдущим номером)
"""

task2_list = [rnd.randint(0, 20) for _ in range(6)]
print(f"Создан список: {task2_list}")

result = 0

for i in range(0, len(task2_list)):
    if task2_list[i] > task2_list[i - 1]:
        result += 1

print(result)