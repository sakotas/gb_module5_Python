import math

# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
#
# print(a)
# print(b)

# Задача 1
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m км?

# kmPerDay = int(input('Введите кол-во километров в день: '))
# distance = int(input('Длина маршрута: '))
#
# print(f'Машина едет со скоростью {kmPerDay} км/день. Расстояние {distance} км она проедет за {(distance + kmPerDay - 1)//kmPerDay} дней')
# print(f'Машина едет со скоростью {kmPerDay} км/день. Расстояние {distance} км она проедет за {distance//kmPerDay + 1} дней')
# print((distance//kmPerDay) + int((distance%kmPerDay) != 0))
# print(math.ceil(distance/kmPerDay))

# Задача 2
# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов:
# Выведите наименьшее число парт, которое нужно приобрести для них.

firstClass = int(input('Введите количество учащихся в первом классе: '))
secondClass = int(input('Введите количество учащихся во втором классе: '))
thirdClass = int(input('Введите количество учащихся в третьем классе: '))

print(firstClass, secondClass, thirdClass)
ClassCollection = [firstClass, secondClass, thirdClass]

result = int()
for i in ClassCollection:
    result = result + i//2 + bool(i%10 != 0)

print(result)


