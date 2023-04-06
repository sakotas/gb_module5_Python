# def summa(num: int):
#     if num == 0:
#         return num
#     return num + summa(num-1)
#
#
# print(summa(10))

"""
Последовательность Фибоначчи с рекурсией

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

Fn = Fn-1 + Fn-2
"""

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
#
# nterms = int(input("Введите количество элементов: "))
#
# if nterms <= 0:
#     print("Пожалуйста, введите положительное число")
# else:
#     print("Последовательность Фибоначчи:")
#     for i in range(nterms):
#         print(fibonacci(i))


"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
"""


def prosto(n: int) -> bool:
    count = 0
    for chislo in range(1, n + 1):
        if n % chislo == 0:
            count += 1

    if count == 2:
        return True

for i in range(1, 10):
    if prosto(i): print(f'Число {i} - простое')
