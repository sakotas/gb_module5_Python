# numbers = '12345678'
# print(numbers)
#
# res_numbers = list(map(int, numbers))
# print(res_numbers)
# #
# # res_numbers = list(filter(lambda x: x % 2 == 0, res_numbers))
# # print(res_numbers)
#
# res_numbers = list(enumerate(len(res_numbers), res_numbers))
# import random
#
# numbers = [random.randint(0, 100) for _ in range(10)]
# letters = list('abdsrtgswd')
#
# print(numbers)
# print(letters)
#
# res_list = list(zip(numbers, letters))
#
# print(res_list)

# for i, item in enumerate(numbers, 100):
#     print(i, item)

# print((lambda x, y, z: x + y + z)(1, 2))

"""
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
по которой вращается самая далекая планета. Круговые орбиты не учитывайте:
вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
"""
import math
import random

planets = [(random.randint(0, 20), random.randint(0, 20)) for _ in range(5)]

print(planets)


def find_farthest_orbit(list_of_orbits):
    planet_sizes = list()

    list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    for i in range(len(list_of_orbits)):
        planet_sizes.append(list_of_orbits[i][0] * list_of_orbits[i][1] * math.pi)
    result = max(planet_sizes)
    return result

print(find_farthest_orbit(planets))
