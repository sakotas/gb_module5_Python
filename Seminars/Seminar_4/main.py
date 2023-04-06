import collections as coll
import random

"""
Напишите программу, которая принимает на вход строку, и отслеживает,
сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
"""

# in_string = str(input("Введите символы: "))
# my_list = list(in_string)
# my_dict = dict()
# for item in list(set(my_list)):
#     my_dict.setdefault(item, 0)
#
# for key, value in my_dict.items():
#     for i in range(len(my_list)):
#         if my_list[i] == key:
#             if value > 0:
#                 my_list[i] = f'{key}_{value}'
#             value += 1
#             my_dict[key] = value
#
# od_results = coll.OrderedDict(sorted(my_dict.items()))
# result_str = ''
#
# for i in my_list:
#     result_str += f'{i} '
#
# print(result_str)
#
# for key, value in od_results.items():
#     print(f"{key} - {value}")

"""
Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки.О
пределите, сколько различных слов содержится в этом тексте.
"""
#
# in_string = input("Введите фразу: ")
#
# strings = in_string.split()
#
# for i in range(len(strings)):
#     strings[i] = strings[i].lower()
#
# my_dict = dict()
#
# for item in list(set(strings)):
#     my_dict.setdefault(item, 0)
#
# for key, value in my_dict.items():
#     count = 0
#     for i in range(len(strings)):
#         if key == strings[i]:
#             count = count + 1
#             my_dict[key] = count
#
# print(my_dict)
#
# print(my_dict)

"""
Написать программу, которая состоит 4 из этапов:
- создает список из рандомных четырехзначных чисел
- принимает с консоли цифру и удаляет ее из всех элементов списка
- цифры каждого элемента суммирует пока результат не станет однозначным числом
- из финального списка убирает все дублирующиеся элементы
- после каждого этапа выводить результат в консоль
Пример:
- 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
- 2 этап: Введите цифру: 3
- 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
- 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
- 3 этап: [3, 1, 5, 5, 3, 5, 4]
- 4 этап: [3, 1, 5, 4]
"""

list_length = int(input("Введите длину списка: "))

list_phase_1 = list()

for i in range(list_length):
    list_phase_1.append(random.randint(1000, 9999))

print()
print("****** Родили список: ******")
print(list_phase_1)
print()

del_number = str(input("Введите число, которое нужно удалить: "))

str_list = list()

for i in range(len(list_phase_1)):
    str_list.append(str(list_phase_1[i]))

print(str_list)

for i in range(len(str_list)):
    str_list[i] = str_list[i].replace(del_number, '')

print(str_list)

for i in range(len(str_list)):
    while len(str_list[i]) > 1:
        temp_list = str_list[i]
        result = 0
        for j in range(len(temp_list)):
            result += int(temp_list[j])
            str_list[i] = str(result)

print(str_list)

print(set(str_list))
